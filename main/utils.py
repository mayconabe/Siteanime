class Animes:

	def __init__(self, temporada=None, titulo=None, sinopse=None, duracao=None, linha=None):
		if linha:
			valores = linha.split(';')
			self.id_ = int(valores[0])
			self.nome = valores[1]
			self.sobrenome = valores[2]
			self.telefone = int(valores[3])
		else:
			self.id_ = id_
			self.nome = nome
			self.sobrenome = sobrenome
			self.telefone = telefone


	def print_linha(self):
		return '{};{};{};{}\n'.format(self.id_, self.nome, self.sobrenome, self.telefone)


	def foto_url(self):
		return '/media/img/{}.png'.format(self.id_)

		
class Banco:

	def __init__(self, caminho=None):
		if caminho:
			self.caminho = caminho
		else:
			self.caminho = 'cadastro.csv'


	def ultimo_id(self):
		contatos = self.get_contatos()
		if len(contatos) > 0:
			return contatos[-1].id_
		else:
			return 0

	def get_contatos(self, id_=None):
		contatos = []
		with open(self.caminho, 'r+') as f1:
			for linha in f1.readlines():
				if linha != '':
					c = Contato(linha=linha)
					if c.id_ == id_:
						return c
					contatos.append(c)
		return contatos


	def salvar_contato(self, c):
		contatos = self.get_contatos()
		if c.id_ == None:
			c.id_ = self.ultimo_id() + 1
			contatos.append(c)
			self.set_contatos(contatos)
		else:
			contatos_aux = []
			for ci in contatos:
				if ci.id_ != c.id_:
					contatos_aux.append(ci)
				else:
					contatos_aux.append(c)
			self.set_contatos(contatos_aux)
		return c.id_


	def set_contatos(self, contatos):
		with open(self.caminho, 'w') as f1:
			for c in contatos:
				f1.write(c.print_linha())




