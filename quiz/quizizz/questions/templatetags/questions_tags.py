from django import template
from questions.models import *

register = template.Library()

def get_categories():
    return Quiz.objects.all()