from django.contrib import admin

from .models import Customers, Drivers, Schedule

# Register your models here.

admin.site.register(Drivers)
admin.site.register(Customers)
admin.site.register(Schedule)
