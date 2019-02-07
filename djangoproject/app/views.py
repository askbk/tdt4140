from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse, Http404
from app.models import Advert

#get_list_or_404() henter liste vha filter

def index(request):  #Se urls.py for å se når denne aktiveres
    all_adverts = get_list_or_404(Advert)
    context = {
        'all_adverts': all_adverts
    }
    return render(request, 'index.html', context)

def advert(request, id): #Se urls.py for å se når denne aktiveres
    advert = get_object_or_404(Advert, id=id)
    context = { #Hvilke variabler vil vi sende til html-dokumentet?
        'advert': advert
    }
    return render(request, 'advert.html', context) #sender besøkende til html-dokumentet
