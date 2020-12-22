from django.contrib import admin
from .models import Task, Contact, Crop, Program

# Register your models here.
admin.site.register(Task)
admin.site.register(Contact)
admin.site.register(Crop)
admin.site.register(Program)

