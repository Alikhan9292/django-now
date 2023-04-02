from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Quiz(models.Model):
    name = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    content = models.TextField(blank=True,  verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True,  verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    email = models.EmailField(null=True)
    message = models.TextField(default='Hello')


    def save(self, *args, **kwargs):
        if not self.id:
            self.time_create = timezone.now()
        self.time_update = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('quiz-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Викторина'
        verbose_name_plural = 'Викторины'

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name = 'Вопросы'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField()


    class Meta:
        verbose_name = 'Ответ'


class QuizTaker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Составитель викторин'

