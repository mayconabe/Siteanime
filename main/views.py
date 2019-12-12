from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
import csv
from django.core.files.storage import FileSystemStorage
from main.models import Anime, Episodio, Temporada
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

ERROS = {
	403: 'Você nao tem permissão para entrar',
	404: 'Pagina não encontrada',
	500: 'Erro interno'
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

class LoginView(View):

	def get(self, request):
		return render(request, 'main/login.html', None)

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
		else:
			return HttpResponseRedirect(reverse('error', kwargs={'tipo_erro': 403}))

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

		
