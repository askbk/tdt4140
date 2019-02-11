from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Startup





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
