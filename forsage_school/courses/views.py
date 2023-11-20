from django.shortcuts import render,redirect,get_object_or_404,redirect
from .models import Course,Question

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def about(request):
    return render(request, 'courses/about.html')

def kontakt(request):
    return render(request, 'courses/kontakt.html')

def start_quiz(request):
    # Получение первого вопроса
    question = get_next_question(request)

    if not question:
        # Все вопросы отвечены, перейти к результатам
        return redirect('quiz_results')

    context = {'question': question}
    return render(request, 'courses/start_quiz.html', context)

def get_next_question(request):
    # Находим следующий неотвеченный вопрос
    answered_questions = request.session.get('answered_questions', set())
    question = Question.objects.exclude(id__in=answered_questions).first()
    return question

def answer_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    user_answer_str = request.POST.get('user_answer')

    if user_answer_str is not None:
        try:
            user_answer = int(user_answer_str)
        except ValueError:
            pass
        else:
            if user_answer == question.correct_option:
                # Правильный ответ, увеличиваем счетчик в сессии
                request.session['score'] = request.session.get('score', 0) + 1

    # Отмечаем вопрос как отвеченный, добавляя его ID в список
    answered_questions = request.session.get('answered_questions', [])
    answered_questions.append(question.id)
    request.session['answered_questions'] = answered_questions

    next_question = get_next_question(request)

    if not next_question:
        return redirect('quiz_results')

    context = {'question': next_question}
    return render(request, 'courses/question.html', context)

def quiz_results(request):
    # Получаем счет из сессии
    
    score = request.session.get('score', 0)
    context = {'score': score}
    return render(request, 'courses/results.html', context)

def reset_quiz(request):
    # Сброс счета пользователя и списка отвеченных вопросов
    request.session['score'] = 0
    request.session['answered_questions'] = []
    return redirect('start_quiz')



from .models import Question

def quiz_results(request):
    # Получите все вопросы и соответствующие правильные ответы
    questions = Question.objects.all()
    

    # Рассчитайте баллы пользователя на основе количества правильных ответов
    
    score = request.session.get('score', 0)

    context = {
        'questions': questions,
        'score': score,
    }

    return render(request, 'courses/results.html', context)


def result_view(request):
    questions = Question.objects.all()
    return render(request, 'results.html', {'questions': questions})