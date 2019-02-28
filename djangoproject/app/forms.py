from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Address, Startup, Tag, Person, Advert, Investor
from django.forms import ModelForm
import datetime


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['postal_code', 'city', 'street_address', 'country']

class StartupForm(ModelForm):
    class Meta:
        model = Startup
        fields = ['bio', 'phase', 'tags', 'employees','user', 'homepage','image']
        widgets = {'tags': forms.CheckboxSelectMultiple()}
        exclude = ('user','address')

class InvestorForm(ModelForm):
    class Meta:
        model = Investor
        fields = ['bio','tags','image']
        widgets = {'tags': forms.CheckboxSelectMultiple()}
        exclude = ('user','address')

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['bio']
        exclude = ('user','address')

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "Name")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'fullname', 'email')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if len(self.cleaned_data["fullname"].split(None, 1)) > 1:
            user.first_name, user.last_name = self.cleaned_data["fullname"].split(None, 1)
        else:
            user.first_name = self.cleaned_data["fullname"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UpdateForm(ModelForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "Name")

    class Meta:
        model = User
        fields = ['fullname', 'email']

    def save(self, commit=True):
        user = super(UpdateForm, self).save(commit=False)
        if len(self.cleaned_data["fullname"].split(None, 1)) > 1:
            user.first_name, user.last_name = self.cleaned_data["fullname"].split(None, 1)
        else:
            user.first_name = self.cleaned_data["fullname"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class AdvertForm(ModelForm):
    """Form for å opprette nye jobbannonser."""
    class Meta:
        model = Advert
        fields = ['title', 'deadline', 'available_positions', 'description']
        initial = {
            'deadline': datetime.datetime.now().isoformat('T')[:10]
        } # DETTE MÅ FIKSES

    def save(self, startup_id, commit=True):
        advert = super(AdvertForm, self).save(commit=False)
        advert.startup = Startup.objects.get(user_id=startup_id)
        if commit:
            advert.save()
        return advert
