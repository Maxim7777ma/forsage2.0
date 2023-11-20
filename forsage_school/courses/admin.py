from django.contrib import admin
from .models import Course,Question,UserProfile

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'duration')  

admin.site.register(Course, CourseAdmin)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'correct_option',)  # Добавьте поля, которые вы хотите отображать в административной панели.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'score',)  # Добавьте поля, которые вы хотите отображать в административной панели.

