from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from app.models import Advert, Startup, Tag, Phase, Address, Content, ContentType, Investor, Person
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from app.forms import StartupForm, AddressForm, RegisterForm, AdvertForm, PersonForm, UpdateForm
from django.contrib.auth.decorators import login_required
#get_list_or_404() henter liste vha filter


def intro(request):
    contents = get_list_or_404(Content)
    types = get_list_or_404(ContentType)

    context = {
    'contents': contents,
    'types': types,
    }
    return render(request, 'intro.html', context)

def index(request):  #Se urls.py for å se når denne aktiveres
    contents = get_list_or_404(Content)
    types = get_list_or_404(ContentType)

    context = {
    'contents': contents,
    'types': types,
    }
    return render(request, 'index.html', context)

def content(request, id):
    content = get_object_or_404(Content, id=id)
    context = {
        'content': content
    }
    return render(request, 'content.html', context)

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
    startup_form = StartupForm(request.POST, request.FILES)
    context = {
        'user_form': user_form,
        'address_form': address_form,
        'startup_form': startup_form,
    }
    if request.method == 'POST':
        if user_form.is_valid() and startup_form.is_valid() and address_form.is_valid():
            user_form.save()
            address_form.save()
            temp = startup_form.save(commit=False)
            temp.user = User.objects.latest('date_joined')
            Group.objects.get(name='Startup').user_set.add(temp.user)
            temp.address = Address.objects.all().order_by("-id")[0]
            temp.save()
            startup_form.save_m2m()
            return HttpResponseRedirect('/profile/'+str(request.user.id))
    return render(request, 'register_startup.html', context)

def register_person(request):
    user_form = RegisterForm(request.POST)
    address_form = AddressForm(request.POST)
    person_form = PersonForm(request.POST,request.FILES)
    context = {
        'user_form': user_form,
        'address_form': address_form,
        'person_form': person_form,
    }
    if request.method == 'POST':
        if user_form.is_valid() and address_form.is_valid() and person_form.is_valid():
            user_form.save()
            address_form.save()
            temp = person_form.save(commit=False)
            temp.user = User.objects.latest('date_joined')
            Group.objects.get(name='Person').user_set.add(temp.user)
            temp.address = Address.objects.all().order_by("-id")[0]
            temp.save()
            return HttpResponseRedirect('/profile/'+str(request.user.id))
    return render(request, 'register_person.html',context)

@login_required
def edit_profile(request):
    user = request.user
    group = user.groups.first()
    print(group)
    if str(group) == "Startup":
        return HttpResponseRedirect("/edit_startup/")
    elif str(group) == "Person":
        return HttpResponseRedirect("/edit_person/")
    elif str(group) == "Investor":
        return HttpResponseRedirect("/edit_investor/")
    else:
        return HttpResponseRedirect("/index/")
@login_required
def edit_startup(request):
    user = request.user
    group = user.groups.first()
    if str(group) == "Startup":
        startup = get_object_or_404(Startup, user_id=user.id)
        address = startup.address
        if request.method == 'POST':
            user_form = UpdateForm(request.POST, instance=user, initial={'fullname': user.first_name + " " + user.last_name})
            address_form = AddressForm(request.POST, instance=address)
            startup_form = StartupForm(request.POST,request.FILES, instance=startup)
            if user_form.is_valid() and address_form.is_valid() and startup_form.is_valid():
                user_form.save()
                address_form.save()
                startup_form.save()
                return HttpResponseRedirect("/profile/"+str(user.id)+"/")
        else:
            user_form = UpdateForm(instance=user, initial={'fullname': user.first_name + " " + user.last_name})
            address_form = AddressForm(instance=address)
            startup_form = StartupForm(instance=startup)

        context = {
            'user_form': user_form,
            'address_form': address_form,
            'startup_form': startup_form,
        }
        return render(request, 'edit_startup.html',context)
    else:
        return HttpResponseRedirect("/index/")

@login_required
def edit_person(request):
    user = request.user
    group = user.groups.first()
    if str(group) == "Person":
        person = get_object_or_404(Person, user_id=user.id)
        address = person.address
        if request.method == 'POST':
            user_form = UpdateForm(request.POST, instance=user, initial={'fullname': user.first_name + " " + user.last_name})
            address_form = AddressForm(request.POST, instance=address)
            person_form = PersonForm(request.POST,request.FILES, instance=person)
            if user_form.is_valid() and address_form.is_valid() and person_form.is_valid():
                user_form.save()
                address_form.save()
                person_form.save()
                return HttpResponseRedirect("/profile/"+str(user.id)+"/")
        else:
            user_form = UpdateForm(instance=user, initial={'fullname': user.first_name + " " + user.last_name})
            address_form = AddressForm(instance=address)
            person_form = PersonForm(instance=person)
        context = {
            'user_form': user_form,
            'address_form': address_form,
            'person_form': person_form,
        }
        return render(request, 'edit_person.html',context)
    else:
        return HttpResponseRedirect("/index/")

@login_required
def edit_investor(request):
    user = request.user
    group = user.groups.first()
    if str(group) == "Investor":
        investor = get_object_or_404(Investor, user_id=user.id)
        if request.method == 'POST':
            user_form = UpdateForm(request.POST, instance=user, initial={'fullname': user.first_name + " " + user.last_name})
            investor_form = InvestorForm(request.POST,request.FILES, instance=investor)
            if user_form.is_valid() and investor_form.is_valid():
                user_form.save()
                investor_form.save()
                return HttpResponseRedirect("/profile/"+str(user.id)+"/")
        else:
            user_form = UpdateForm(instance=user, initial={'fullname': user.first_name + " " + user.last_name})
            investor_form = InvestorForm(instance=investor)
        context = {
            'user_form': user_form,
            'person_form': person_form,
        }
        return render(request, 'edit_investor.html',context)
    else:
        return HttpResponseRedirect("/index/")


def register_investor(request):
    return render(request, 'index.html')


def profile(request, id):
    user = User.objects.get(id=id)
    if user.groups.filter(name='Startup').exists():
        profile = Startup.objects.get(user_id=id)
    elif user.groups.filter(name="Person").exists():
        profile = Person.objects.get(user_id=id)
    elif user.groups.filter(name="Investor").exists():
        profile = Investor.objects.get(user_id=id)
    # elif user.is_superuser:
    #     return HttpResponseRedirect('/admin/')
    else:
        profile = ""
    context = {
        'profile_user': user, #user objekt til den profilen du besøker
        'profile': profile, #Startup/Investor/Person objekt
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
    tags = list(get_list_or_404(Tag))

    for startup in startups:
        s_tags = list(startup.tags.all())
        tagslist = " ".join(list(map(lambda a: a.title, s_tags)))
        startup.tagslist = tagslist

    phases = get_list_or_404(Phase)
    context = {
        'startups': startups,
        'phases': phases,
        'tags': tags,
    }
    return render(request, "startups.html", context)

def adverts(request):
    adverts = get_list_or_404(Advert)
    addresses = get_list_or_404(Address)
    #   Lager en liste med alle byene det finner startups i
    cities = set(map(lambda a: a.city, addresses))
    tags = list(get_list_or_404(Tag))

    for advert in adverts:
        s_tags = list(advert.startup.tags.all())
        tagslist = " ".join(list(map(lambda a: a.title, s_tags)))
        advert.startup.tagslist = tagslist

    context = {
        'adverts': adverts,
        'cities': cities,
        'tags': tags,
    }
    return render(request, "adverts.html", context)

@login_required(login_url='/login/')
def new_advert(request):
    advert_form = AdvertForm(request.POST)
    context = {
        'advert_form': advert_form,
    }
    if request.method == 'POST':
        if advert_form.is_valid():
            advert_form.save(request.user.id)
            return HttpResponseRedirect("/adverts/")
    return render(request, 'new_advert.html', context)

def investors(request):
    return render(request, "investors.html")
