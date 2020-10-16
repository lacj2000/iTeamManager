from django.shortcuts import render

# Create your views here.

def singin(request):
    contexto = {}
    arquivo = 'signin_page/signin.html'
    return render(request, arquivo, contexto)

def profile(request, user_id):
    contexto = {'user':{'user_id':5,'name':'Elmo','image_profile':'/media/images/12345678.png',
    'email':'teste1234@teste.tst' }}
    arquivo = 'profile/profile.html'
    return render(request, arquivo, contexto)


