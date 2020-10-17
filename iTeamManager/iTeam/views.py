from django.shortcuts import render
from iTeam.models import Project, Researcher


def main_page(request):
    contexto = {}
    arquivo = 'main_page/main-page.html'
    return render(request, arquivo, contexto)


def singin(request):
    contexto = {}
    arquivo = 'signin_page/signin.html'
    return render(request, arquivo, contexto)


def profile(request, user_id):
    user = Researcher.objects.get(id=user_id)
    projects = Project.objects.filter(researchers__id = user_id)
   
    contexto = {'user': user, 'projects':projects}
    arquivo = 'profile/profile.html'
   
    return render(request, arquivo, contexto)


