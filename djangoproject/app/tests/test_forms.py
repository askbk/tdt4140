from django.test import TestCase
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Address, Startup, Tag, Person, Advert, Phase
from app.forms import RegisterForm, InvestorForm, StartupForm, AddressForm, PersonForm
from django.forms import ModelForm

class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="usertest@usertest.no", password1="User12345", password2="User12345", fullname="user", username="test",)

class RegisterForm_Test(TestCase):
    # Valid Form Data
    def test_Registerform_valid(self):
        form = RegisterForm(data={'email': "usertest@usertest.no", 'fullname': "user", 'password1': "User123456", 'password2':"User123456",'username':"test"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_Registerform_invalid(self):
        form = RegisterForm(data={'email': "", 'fullname': "mp"})
        self.assertFalse(form.is_valid())

class PersonForm_Test(TestCase):
    # Valid Form Data
    def test_PersonForm_valid(self):
        form = PersonForm(data={'email': "usertest@usertest.no", 'fullname': "user", 'password1': "User123456", 'password2':"User123456",'username':"test",'bio':"fwegwe", 'postal_code':"0976", 'city':"Trondheim", 'street_address': "Gløs 11 B", 'country': "Norway"})
        self.assertTrue(form.is_valid())


class InvestorForm_Test(TestCase):
    # Valid Form Data
    def test_InvestorForm_valid(self):
        form = InvestorForm(data={'bio':"24"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_InvestorForm_invalid(self):
        form = InvestorForm(data={'email': "usertest@usertest.no", 'fullname': "user", 'password1': "User123456", 'password2':"User123456",'username':"test",'bio':"fwegwe", 'postal_code':"0976", 'city':"Trondheim", 'street_address': "Gløs 11 B", 'country': "Norway", 'tags': "Engineering",'image': ""})
        self.assertFalse(form.is_valid())

class StartupForm_Test(TestCase):
    # Valid Form Data
    def test_StartupForm_valid(self):
        #phases = Phase.objects.get(id=1)
        #tags = Tag.objects.all()
        #form = StartupForm(data={'bio':"24", 'tags':tags,'phase':2})
        #self.assertTrue(form.is_valid())
        return None

    # Invalid Form Data
    def test_StartupForm_invalid(self):
        form = StartupForm(data={'email': "usertest@usertest.no", 'fullname': "user", 'password1': "User123456", 'password2':"User123456",'username':"test",'bio':"fwegwe", 'postal_code':"0976", 'city':"Trondheim", 'street_address': "Gløs 11 B", 'country': "Norway", 'tags': "Engineering",'image':"images/no-image.png",'employees':"10", 'homepage':""})
        self.assertFalse(form.is_valid())

class AddressForm_Test(TestCase):
    # Valid Form Data
    def test_AddressForm_valid(self):
        form = AddressForm (data={'postal_code':"0976", 'city': "Oslo", 'street_address': "Teppeveien 22B", 'country': "Mongolia"})
        self.assertTrue(form.is_valid())

    def test_AddressForm_invalid(self):
        form = AddressForm (data={'postal_code':"", 'city': "Oslo", 'street_address': "Teppeveien 22B", 'country': "Mongolia"})
        self.assertFalse(form.is_valid())
