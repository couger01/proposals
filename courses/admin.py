from django.contrib import admin

# Register your models here.
from .models import Course, Department, Proposal, Stage, Faculty

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Proposal)
admin.site.register(Stage)
admin.site.register(Faculty)
