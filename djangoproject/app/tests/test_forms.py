from django.test import TestCase
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Address, Startup, Tag, Person, Advert
from django.forms import ModelForm

class UserTest(TestCase):
    def test_user_registration(self):
        pw_mismatch = {"username": "Bankchain", "password1": "passord1", "passord2": "passord2"}
        user_creation_form = UserCreationForm(data=pw_mismatch)
        self.assertTrue(not user_creation_form.is_valid())
        pw_match = {"username": "Bankchain", "password1": "passord1", "passord2": "passord1"}
        user_creation_form = UserCreationForm(data=pw_match)
        self.assertTrue(user_creation_form.is_valid())
