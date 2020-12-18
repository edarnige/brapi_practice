from django.contrib import admin
from .models import Task, Contact, Crop

# Register your models here.
admin.site.register(Task)
admin.site.register(Contact)
admin.site.register(Crop)