from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_limite = models.DateField(null=True, blank=True)
    public = models.BooleanField(default=False)
    shared = models.BooleanField(default=False)
    shared_with = models.ManyToManyField(User, related_name='shared_tasks', blank=True)

    def _str_(self):  
      return self.title + ' - ' + self.user.username
# Create your models here.
