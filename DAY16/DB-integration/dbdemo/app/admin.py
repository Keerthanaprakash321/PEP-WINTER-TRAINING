from django.contrib import admin
from .models import Driver, Car, student, personal


admin.site.register(Driver)
admin.site.register(Car)

admin.site.register(student)
admin.site.register(personal)