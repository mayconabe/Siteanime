from django.db import models
from django.conf import settings
from django.contrib.auth.models import User as DjangoUser


# Create your models here.
TIPO = [
	('N', 'Normal'),
	('F', 'Filler'),
	('filme', 'Filme'),
	('ova', 'OVA')
]

GENEROS = [
	('acao', 'Ação'),
	('comedia', 'Comédia'),
	('aventura', 'Aventura'),
	('sliceoflife', 'Slice of life'),
	('romance', 'Romance'),
	('ecchi', 'Ecchi'),
	('faroeste', 'Faroeste'),
	('scifi', 'Sci-Fi'),
	('horror', 'Terror'),
	('guerra', 'Guerra'),
	('policial', 'Policial'),
	('investigacao', 'Investigação'),
	('artesmarciais', 'Artes Marciais'),
	('isekai', 'Isekai'),
	('shoujo', 'Shoujo'),
	('josei', 'Josei'),
	('shounen', 'Shounen'),
	('kodomo', 'Kodomo'),
]

TAGS = [
	('violencia', 'violencia'),
	('linguagem ofensiva', 'Linguagem Ofensiva'),
	('ecchi', 'Ecchi'),
]



class Tag(models.Model):

	tipo_tag = models.CharField(choices=TAGS, max_length=20)

	def __str__(self):
		return self.get_tipo_tag_display()


class Genero(models.Model):

	tipo_genero = models.CharField(choices=GENEROS, max_length=20)

	def __str__(self):
		return self.get_tipo_genero_display()


class Anime(models.Model):

	nome = models.CharField(max_length=200)
	avaliacao = models.IntegerField()
	generos = models.ManyToManyField(Genero)
	tags = models.ManyToManyField(Tag)
	sinopse = models.CharField(max_length=600)
	class_indicativa = models.IntegerField()
	imagem = models.CharField(max_length=200)
	visualizacoes = models.IntegerField(default=0)

	@property
	def ult_episodio(self):
		eps = Episodio.objects.filter(temporada__anime=self)
		if len(eps) == 0:
			return None
		else:
			return eps[0]


	@property
	def capa(self):
		return '/media/img/{0}/{1}.png'.format(self.imagem, self.id)


	def __str__(self):
		return self.nome



class Temporada(models.Model):

	anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
	numero = models.IntegerField()
	nome = models.CharField(max_length=200)

	def __str__(self):
		return self.anime.nome + ' - ' + str(self.numero)


class Episodio(models.Model):

	temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
	numero = models.IntegerField()
	titulo = models.CharField(max_length=200)
	sinopse = models.CharField(max_length=1000)
	duracao = models.IntegerField()
	tipo = models.CharField(choices=TIPO, max_length=200)
	tags = models.ManyToManyField(Tag)
	data_criacao = models.DateTimeField('Data de criação')
	data_adicao = models.DateTimeField('Data de Adição')
	imagem = models.CharField(max_length=200)
	curtidas = models.IntegerField(default=0)
	naogostei = models.IntegerField(default=0)

	def __str__(self):
		return self.titulo

	@property
	def source(self):
		return '/media/episodios/{0}/{1}.mp4'.format(self.temporada.anime.nome, self.numero)

	def m1_curti(self, valor):
		if valor in [1, -1]:
			self.curtidas += valor
		else:
			raise Exception("Valor só pode 1 ou -1")

	def naogostei(self, valor):
		if valor in [1, -1]:
			self.naogostei += valor
		else:
			raise Exception("Valor só pode 1 ou -1")



class Audio(models.Model):

	episodio = models.ForeignKey(Episodio, on_delete=models.CASCADE)
	lingua = models.CharField(max_length=200)

	def __str__(self):
		return self.lingua


class Legenda(models.Model):

	episodio = models.ForeignKey(Episodio, on_delete=models.CASCADE)
	lingua = models.CharField(max_length=200)
	caminho = models.CharField(max_length=200)

	def __str__(self):
		return self.lingua

class Perfil(models.Model):

	djangouser = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
	telefone = models.IntegerField()

	def nome_de_usuario(self):
		if self.djangouser.first_name != '' and self.djangouser.last_name != '':
			return self.djangouser.first_name + ' ' + self.djangouser.last_name
		elif self.djangouser.first_name != '' and self.djangouser.last_name == '':
			return self.djangouser.first_name
		else:
			return self.djangouser.username

class PerfilAnime(models.Model):
	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
	anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
	episodio = models.ForeignKey(Episodio, on_delete=models.CASCADE)
	momento = models.IntegerField()
	favorito = models.BooleanField()
	notificacoes = models.BooleanField()

class PerfilEpisodio(models.Model):

	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
	episodio = models.ForeignKey(Episodio, on_delete=models.CASCADE)
	_curti = models.BooleanField(default=False)
	_naogostei = models.BooleanField(default=False)

	def curti(self, valor=True):
		if valor == True:
			self._curti = True
			self.episodio.m1_curti(1)
		else:
			self._curti = False
			self.episodio.m1_curti(-1)

	def naogostei(self, valor=True):
		if valor == True:
			self._curti = True
			self.episodio.m1_naogostei(1)
		else:
			self._curti = False
			self.naogostei(-1)