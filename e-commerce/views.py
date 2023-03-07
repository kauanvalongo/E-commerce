from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, get_user_model
from .forms import ContactForm


# Create your views here.
def home(request):
    print(request.session.get('first_name', 'Unknow'))

    context = {
        "title": "Página principal",
        "content": "Bem-vindo a página principal"
        }
    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
    return render(request, 'home.html', context)


def about_page(request):
    context = {
        "title": "Página sobre",
        "content": "Bem-vindo a página sobre"
    }
    return render(request, "about/view.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Página de contato",
        "content": "Bem-vindo a página de contato",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    #if request.method == "POST":
        #print(request.POST)
        #print(request.POST.get('Nome_Completo'))
        #print(request.POST.get('email'))
        #print(request.POST.get('Mensagem'))

    return render(request, "contact/view.html",  context)
