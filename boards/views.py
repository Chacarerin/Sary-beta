

# Create your views here.
#from django.http import HttpResponse
#from django.shortcuts import render

#def index(request):
   # return HttpResponse("Mensaje, Hola Mundo.")
from django.views.generic import TemplateView

class IndexPageView(TemplateView):
    template_name="index.html"