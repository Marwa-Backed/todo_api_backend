
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=20, default="#a29bfe")
python todo_api/manage.py makemigrations
python todo_api/manage.py migrate
    def __str__(self):
        return self.title