from django.contrib import admin
from .models import Address, Phase, Tag, Startup, Person, Investor, Advert, Content, ContentType, Message

# Register your models here.
admin.site.register(Address)
admin.site.register(Phase)
admin.site.register(Tag)
admin.site.register(ContentType)

admin.site.register(Startup)
admin.site.register(Person)
admin.site.register(Investor)
admin.site.register(Advert)
admin.site.register(Content)
admin.site.register(Message)
