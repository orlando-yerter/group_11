from django.shortcuts import render,redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    formulario_contacto=FormularioContacto()
    return render(request, "contact/contact.html", {'miFormulario':formulario_contacto})


