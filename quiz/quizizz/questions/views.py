from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError

from .models import *
from django.shortcuts import render, redirect
from .forms import QuizForm
from django.shortcuts import render
from .models import Question, Quiz, Answer

def quiz_detail(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        # Получаем ответы пользователя из запроса и проверяем их
        correct_count = 0
        for question in questions:
            selected_answer = request.POST.get('q{}'.format(question.id))
            if selected_answer:
                answer = Answer.objects.get(id=selected_answer)
                if answer.is_correct:
                    correct_count += 1
        return render(request, 'quiz_results.html', {'correct_count': correct_count})
    else:
        return render(request, 'quiz.html', {'questions': questions})


def contact(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            # Обработка валидной формы
            # Перенаправление на страницу "Спасибо за сообщение"
            return redirect('thanks')
    else:
        form = QuizForm()
    context = {'form': form}
    return render(request, 'questions/contact.html', context)

def thanks(request):
    return render(request, 'questions/thanks.html')


def index(request):
    posts = Quiz.objects.filter(is_published=True)
    return render(request, 'questions/index.html', {'posts': posts})
def quiz(request):
    return render(request, 'questions/index.html')

def about(request):
    return render(request, 'questions/about.html')

def quiz_detail(request):
    # реализация логики для отображения викторины
    return render(request, 'questions/quiz_detail.html')

def categories(request, catid):
    if (request.POST):
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1>{catid}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def badRequest(request, exception):
    return HttpResponseBadRequest('Плохой запрос')

def permissionDenied(request, exception):
    return HttpResponseForbidden('В разрешении отказано')

def serverError(request):
    return HttpResponseServerError('Внутренняя ошибка сервера')
