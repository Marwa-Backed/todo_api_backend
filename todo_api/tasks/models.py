
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    color = models.CharField(max_length=20, default="#E8F5E9")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title