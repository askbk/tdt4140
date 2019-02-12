from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from app.models import Advert, Startup, Tag, Phase, Address
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.forms import StartupForm, AddressForm, RegisterForm
#get_list_or_404() henter liste vha filter

def index(request):  #Se urls.py for å se når denne aktiveres
    return render(request, 'index.html')

def advert(request, id): #Se urls.py for å se når denne aktiveres
    advert = get_object_or_404(Advert, id=id)
    context = { #Hvilke variabler vil vi sende til html-dokumentet?
        'advert': advert
    }
    return render(request, 'advert.html', context) #sender besøkende til html-dokumentet


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/'+str(request.user.id))
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def register_startup(request):
    user_form = RegisterForm(request.POST)
    address_form = AddressForm(request.POST)
    startup_form = StartupForm(request.POST)
    context = {
        'user_form': user_form,
        'address_form': address_form,
        'startup_form': startup_form,
    }
    if request.method == 'POST':
        if user_form.is_valid() and startup_form.is_valid() and address_form.is_valid():
            user_form.save()
            address_form.save()
            a = startup_form.save(commit=False)
            a.user = User.objects.latest('date_joined')
            a.address = Address.objects.all().order_by("-id")[0]
            a.save()
            return HttpResponseRedirect("/index/")
    return render(request, 'register_startup.html', context)

def register_person(request):
    return render(request, 'index.html')

def register_investor(request):
    return render(request, 'index.html')


def profile(request, id):
    user = User.objects.get(id=id)
    if user.groups.filter(name='Startup').exists():
        profile = Startup.objects.get(user_id=id)

    context = {
        'user': request.user,
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect('/profile/'+str(user.id)+"/")
    return render(request, "login.html", {'wrongdetails': 1})

def logout_user(request):
    auth_logout(request)
    return HttpResponseRedirect('../login')


def startups(request):
    startups = get_list_or_404(Startup)
    phases = get_list_or_404(Phase)
    tags = get_list_or_404(Tag)
    context = {
        'startups': startups,
        'phases': phases,
        'tags': tags,
    }
    return render(request, "startups.html", context)

def adverts(request):
    adverts = get_list_or_404(Advert)
    context = {
        'adverts': adverts
    }
    return render(request, "adverts.html", context)

def investors(request):
    return render(request, "investors.html")


'''
def register_startup(request):
    user_form = UserCreationForm(request.POST)
    startup_form = StartupForm()
    address_form = AddressForm()
    context = {
        'user_form': user_form,
        'startup_form': startup_form,
        'address_form': address_form,
    }
    return render(request,'register_startup.html', context)

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return HttpResponseRedirect("/index")
    else:
        #form = UserCreationForm()
        form = SignUpForm()
    return render(request, 'register_startup.html', {'form': form})
'''
