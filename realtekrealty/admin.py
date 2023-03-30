from django.contrib import admin
from .models import register,Uploads,home


admin.site.register(Uploads),
admin.site.register(register),
admin.site.register(home)

# Register your models here.
