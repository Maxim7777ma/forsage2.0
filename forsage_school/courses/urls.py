from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name='about'),
    path('course_list/', views.course_list, name='course_list'),
]