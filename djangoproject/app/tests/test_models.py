from django.test import TestCase
from django.contrib.auth.models import User
from app.models import Address, Phase, Tag, Startup, User
from django.conf import settings

class AddressTest(TestCase):
    def create_address(self):
        return Address.objects.create(postal_code=7042, city="Trondheim", street_address="Dyre Halses Gate 5", country = "Norway")

    def test_address_creation(self):
        w = self.create_address()
        self.assertTrue(isinstance(w, Address))
        self.assertEqual(7042, w.postal_code)
        self.assertEqual("Trondheim", w.city)
        self.assertEqual("Dyre Halses Gate 5", w.street_address)
        self.assertEqual("Norway", w.country)
        self.assertEqual("Dyre Halses Gate 5 - 7042, Trondheim", w.__str__())

class PhaseTest(TestCase):
    def create_phase(self):
        return Phase.objects.create(title="Funding phase")

    def test_phase_creation(self):
        w = self.create_phase()
        self.assertTrue(isinstance(w, Phase))
        self.assertEqual("Funding phase", w.title)
        self.assertEqual("Funding phase", w.__str__())

class TagTest(TestCase):
    def create_tag(self):
        return Tag.objects.create(title="Banking")

    def test_tag_creation(self):
        w = self.create_tag()
        self.assertTrue(isinstance(w, Tag))
        self.assertEqual("Banking", w.title)
        self.assertEqual("Banking", w.__str__())

class StartupTest(TestCase):
    def create_startup(self):
        return Startup.objects.create(
            bio="A blockchain startup with the mission of creating a sustainable
                banking system",
            user=User.objects.create(
                username="Bankchain",
                password="passord1"

            )
        )

    def test_startup_creation(self):
        w = self.create_startup()
        self.assertTrue(isinstance(w, Tag))
        self.assertEqual("Banking", w.title)
        self.assertEqual("Banking", w.__str__())
