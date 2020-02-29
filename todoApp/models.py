from django.db import models
from datetime import datetime


class Task(models.Model):
    note = models.CharField(max_length = 250, blank = False)
    created_on = models.DateTimeField(default= datetime.now)

    def __str__(self):
        return f'Content created on {self.created_on}'
