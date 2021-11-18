from django import forms
from django.forms import fields
from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text'] #campo text no model
        labels = {'text': ''} #campo de preenchimento vazio
