from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    #print("Tipo de petición: {}".format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Suponemos que todo ha ido bien, redireccionamos
            #return redirect(reverse ('contact')+"?ok")
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                #asunto
                "La Caffettiera: Nuevo mensaje de contacto",
                #cuerpo
                "De {} <{}> \n\nEscribió:\n\n{}".format(name, email, content),
                #email_origen
                "no-reply@inbox.mailtrap.io",
                #email_destino
                ["eliaspersa@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #Todo ha ido bien, redireccionamos a OK
                return redirect(reverse ('contact')+"?ok")
            except:
                #Algo no ha ido bien, redireccinamos a FAIL
                return redirect(reverse ('contact')+"?fail")


    return render(request, 'contact/contact.html', {'form':contact_form})