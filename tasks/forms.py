from django.forms import ModelForm
from .models import Task
from .models import Comment


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important', 'public']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
