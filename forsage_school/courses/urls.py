from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name='about'),
    path('course_list/', views.course_list, name='course_list'),
    path('start_quiz/', views.start_quiz, name='start_quiz'),
    path('answer_question/<int:question_id>/', views.answer_question, name='answer_question'),
    path('quiz_results/', views.quiz_results, name='quiz_results'),
    path('reset_quiz/', views.reset_quiz, name='reset_quiz'),
    path('kontakt/', views.kontakt, name='kontakt'),
]