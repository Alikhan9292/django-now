from django.contrib import admin
from .models import Quiz, Question, Answer, QuizTaker

class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'time_create')
    list_display_links = ('id', 'name')
    list_filter = ('is_published',)
    search_fields = ('name', 'description')
    list_per_page = 25

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'quiz')
    list_display_links = ('id', 'text')
    search_fields = ('text', 'quiz__name')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'is_correct', 'question')
    list_display_links = ('id', 'text')
    list_filter = ('is_correct',)
    search_fields = ('text', 'question__text', 'question__quiz__name')

class QuizTakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quiz', 'score', 'date_taken')
    list_display_links = ('id', 'user')
    search_fields = ('user__username', 'quiz__name')
    list_filter = ('quiz', 'score', 'date_taken')

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(QuizTaker, QuizTakerAdmin)
