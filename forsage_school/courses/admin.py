from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'duration')  

admin.site.register(Course, CourseAdmin)