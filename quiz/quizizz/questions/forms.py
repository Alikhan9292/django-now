from django import forms
from pydantic import ValidationError

from .models import Quiz


def validate_name(value):
    if len(value) > 50:
        raise ValidationError('Имя не может быть длиннее 50 символов')


class QuizForm(forms.ModelForm):
    name = forms.CharField(validators=[validate_name])

    class Meta:
        model = Quiz
        fields = ['name', 'description', 'email', 'message']
