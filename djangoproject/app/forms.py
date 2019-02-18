from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Address, Startup, Tag, Person
from django.forms import ModelForm


class AddressForm(ModelForm):
        class Meta:
                model = Address
                fields = ['postal_code', 'city', 'street_address']

class StartupForm(ModelForm):
        # Liste til tags hentes fra databasen
        # tag_list = list(Tag.objects.all())
        # mapped_tag_list = list(map(lambda a: a.title, tag_list))
        # duplicated_mapped_tag_list = [val for val in mapped_tag_list for _ in (0, 1)]
        # it = iter(duplicated_mapped_tag_list)
        # complete_tag_list = tuple(zip(it, it))
        # liste med tags ferdig
        # tags = forms.MultipleChoiceField(choices=complete_tag_list, widget=forms.CheckboxSelectMultiple())
        class Meta:
                model = Startup
                fields = ['bio', 'phase', 'tags', 'employees','user', 'image']
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

"""
class SignUpForm(UserCreationForm):

startupname = forms.CharField(max_length=30, required=True)
email = forms.EmailField(max_length=254)
description = forms.CharField(widget=forms.Textarea)
address = forms.CharField(max_length=30, required=True)
employees = forms.IntegerField(min_value=1) #max_length=2)
address = forms.CharField(max_length=30)
city = forms.CharField(max_length=30)
postnumber = forms.CharField(max_length=4)
startup_fase = forms.ChoiceField(choices=[(1,'Beginning'),(2,'Middle'),(3,'End')])
company_type = forms.ChoiceField(choices=[(1,'Engineering'),(2,'Economy'),(3,'Programming'),(4,'Prototyping')])
#prof = forms.ImageField(upload_to='img/profile') #Funker ikke ennaa, mulig losning

class Meta:
model = User
fields = ('startupname','email','startup_fase','company_type','description','employees','address','city','postnumber', 'password1', 'password2', )

bio =


class Meta:
model = Startup
fields = ('bio','address','employees','phase','tags')
"""
