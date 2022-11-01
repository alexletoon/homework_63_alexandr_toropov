from xml.dom import ValidationErr
from django import forms
from django.forms import widgets 
from task_app.models.status import Status
from task_app.models.type import Type
from task_app.models.task import Task
from django.core.validators import BaseValidator, MinLengthValidator
from django.core.exceptions import ValidationError

# class Valid(BaseValidator):
#      def __init__(self, limit_value=10, message='') -> None:
#          super().__init__(limit_value, message).__init__(limit_value=limit_value, message=message)


def title_length_validator(string):
    if len(string) > 20 or len(string) < 3:
        raise ValidationError('Данная строка должна быть не менее 3х символов, но не более 20')
    return string 


class TaskForm(forms.ModelForm):
    task = forms.CharField(max_length=200, required=True, label='Задача', validators=(title_length_validator,))
    description = forms.CharField(max_length=2000, required=False, label='Описание', widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус', widget=widgets.RadioSelect)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, label='Тип задачи', widget=widgets.RadioSelect)

    class Meta:
        model = Task
        fields = ['task', 'description', 'status', 'type']


