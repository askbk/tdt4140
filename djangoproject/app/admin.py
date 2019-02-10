from django.contrib import admin
from .models import Address, Startup, Person, Investor, Advert

# Register your models here.
admin.site.register(Address)
admin.site.register(Startup)
admin.site.register(Person)
admin.site.register(Investor)
admin.site.register(Advert)
