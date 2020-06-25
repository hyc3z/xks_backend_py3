from django.contrib import admin

from .models import Teacher
from .models import OfferCourse

admin.site.register(Teacher)
admin.site.register(OfferCourse)