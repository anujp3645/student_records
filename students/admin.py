from django.contrib import admin
from .models import student
from .models import Feedback
# Register your models here.
admin.site.register(student)
admin.site.register(Feedback)
