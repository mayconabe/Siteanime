from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
import csv
from django.core.files.storage import FileSystemStorage
from main.models import Anime, Episodio, Temporada
from django.urls import reverse
from main.forms import UserModelForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
)

# Create your views here.

ERROS = {
	403: 'Você não tem permissão para entrar.',
	404: 'Pagina não encontrada.',
	500: 'Erro interno.'
}

class LoggedView(View):

	def dispatch(self, request, *args, **kwargs):

		if not request.user.is_authenticated:
			return HttpResponseRedirect(reverse('login'))
		return super(LoggedView, self).dispatch(request,*args, **kwargs)

class LogoutView(View):

	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('login'))


class IndexView(LoggedView):

	def get(self, request):
		data = {
			'animes': Anime.objects.all(),
			'episodio': Episodio.objects.all()
		}

		return render(request, 'main/index.html', data)

class EpisodioView(LoggedView):

	def get(self, request, id_=None):
		data = {
			'episodio': get_object_or_404(Episodio, pk=id_)
		}
		return render(request, 'main/episodio.html', data)


class ErrorView(View):

	def get(self, request, tipo_erro):
		if tipo_erro not in ERROS:
			tipo_erro = 404
		data = {
			'tipo_erro': tipo_erro,
			'erro': ERROS[tipo_erro],
		}
		return render(request, 'main/erro.html', data)

class MinhaListaView(View):

	def get(self, request):


		return render(request, 'main/minhalista.html', None)

class AnimesView(View):

	def get(self, request):
		data = {
			'animes': Anime.objects.all()
		}
		return render(request, 'main/animes.html', data)

class RecentAddView(View):

	def get(self, request):
		return render(request, 'main/adicionadosrecentemente.html', None)

class CadastroView(View):
	def get(self, request):
		form = UserModelForm()
		return render(request, 'main/signin.html', {'form': form})
	
	def post(self, request):
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			email = request.POST['email']

			user = User.objects.create_user(username=username, password=password, email=email)
			user.save()
			return redirect('login')
		else:
			return render(request, 'main/signin.html')





		
