from django.contrib import admin

from .models import Student
from .models import ChooseCourse

admin.site.register(Student)
admin.site.register(ChooseCourse)