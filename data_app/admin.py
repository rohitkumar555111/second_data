from django.contrib import admin
from .models import Students , Movie, Character , UserProfile

# Register your models here.
admin.site.register(Students)
admin.site.register(Movie)
admin.site.register(Character)
admin.site.register(UserProfile)
