from django.shortcuts import render

# Create your views here.

def singin(request):
    contexto = {}
    arquivo = 'signin_page/signin.html'
    return render(request, arquivo, contexto)


