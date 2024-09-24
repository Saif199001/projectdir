from django.contrib import admin
from .models import courses, workshop, contacts
# Register your models here.

admin.site.register(courses)
admin.site.register(workshop)
admin.site.register(contacts)

