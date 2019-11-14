import json
import urllib
from hashlib import sha1
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, DetailView
from cruds.views import CRUDMixin
from .models import Denuncia


# Create your views here.
class DenunciaCreateView(CRUDMixin, CreateView):
    model = Denuncia
    crud_template_name = 'crear_denuncia.html'
    fields = ['nombre_apellido_sospechoso',
              'apodo_sospechoso',
              'descripcion',
              'locacion']

    def form_valid(self, form):

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        print(self.request.POST)
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''
        cid= None
        if result['success']:
            form.save()
            x= form.save()
            cid=x.pk
            messages.warning(self.request, 'New comment added with success!')
        else:
            messages.warning(self.request, 'Invalid reCAPTCHA. Please try again.')

        return completado(self.request, id=cid) if cid!= None else redirect('/new/')

        
def completado(request, id):

    return render(request, 'completado.html', {"id": id})


