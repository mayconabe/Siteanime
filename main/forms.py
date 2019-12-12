from django.forms import ModelForm
from main.models import Contato
from main.models import Endereco, Telefone

class ContatoForm(ModelForm):

	class Meta:
		model = Contato
		exclude = ['telefone', 'endereco']

class TelefoneForm(ModelForm):

	class Meta:
		model = Telefone
		fields = '__all__'


class EnderecoForm(ModelForm):

	class Meta:
		model = Endereco
		fields = '__all__'