from django.db.models import fields
from django.forms import ModelForm
from .models import *
class TodoForm(ModelForm):
    class Meta:
        model = todo
        fields =['title','descr']

        