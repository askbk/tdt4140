from django.test import TestCase
from app.models import Address

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