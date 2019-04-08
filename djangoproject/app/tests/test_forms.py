from django.test import TestCase
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Address, Startup, Tag, Person, Advert
from django.forms import ModelForm
from .forms import *   # import all forms

class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="usertest@usertest.no", password="user", first_name="user", phone=12345678)

class User_Form_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = UserForm(data={'email': "usertest@usertest.no", 'password': "user", 'first_name': "user", 'phone': 12345678})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = UserForm(data={'email': "", 'password': "mp", 'first_name': "mp", 'phone': ""})
        self.assertFalse(form.is_valid())



'''
class UserTest(TestCase):
    def test_user_registration(self):
        pw_mismatch = {"username": "Bankchain", "password1": "passord1", "passord2": "passord2"}
        user_creation_form = UserCreationForm(data=pw_mismatch)
        self.assertFalse(user_creation_form.is_valid())
        pw_match = {"username": "Chainbank", "password1": "passord1", "passord2": "passord1"}
        user_creation_form = UserCreationForm(data=pw_match)
        self.assertTrue(user_creation_form.is_valid())
'''
