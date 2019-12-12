"""mysite5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import IndexView
from main.views import EpisodioView
from main.views import LoginView
from main.views import ErrorView
from main.views import LogoutView
from main.views import MinhaListaView
from main.views import AnimesView
from main.views import RecentAddView

urlpatterns = [
	#path('novo/', CadastroView.as_view(), name='cadastros'),
	path('', IndexView.as_view(), name='index'),
    path('watch/<int:id_>', EpisodioView.as_view(), name='episodio'),
    path('error/<int:tipo_erro>', ErrorView.as_view(), name='error'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('minhalista/', MinhaListaView.as_view(), name='minhalista'),
    path('animes/', AnimesView.as_view(), name='animes'),
    path('recentadd/', RecentAddView.as_view(), name='recentadd'),
	#path('detalhes/<int:contato_id>', DetalhesView.as_view(), name='detalhes'),
    #path('editar/<int:contato_id>', CadastroView.as_view(), name='editar'),
    #path('delete/<int:contato_id>', DeleteView.as_view(), name='delete')

]
