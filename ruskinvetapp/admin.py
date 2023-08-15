from django.contrib import admin
from .models import Visit
from .models import Pet_Parent
from .models import Pet

# Register your models here.
admin.site.register(Pet_Parent)
admin.site.register(Pet)
admin.site.register(Visit)