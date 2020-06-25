from django.contrib import admin

from .models import SystemAdmin
from .models import Campus
from .models import Term
from .models import School
from .models import Course

admin.site.register(SystemAdmin)
admin.site.register(Campus)
admin.site.register(Term)
admin.site.register(School)
admin.site.register(Course)