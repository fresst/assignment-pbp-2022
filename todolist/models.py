from django.contrib.auth.models import User
from django.db import models
from django import forms

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
                User,
                models.SET_NULL,
                blank=True,
                null=True
            )
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def change_status(self):
        self.is_finished = not self.is_finished
        self.save()

class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description')
        widgets = {
            'description': forms.Textarea(),
        }