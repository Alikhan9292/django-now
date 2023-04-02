from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('quiz/', quiz, name='quiz'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('quiz_detail/', quiz_detail, name='quiz_detail'),
    path('thanks/', thanks, name='thanks')
]