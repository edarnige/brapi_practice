from django.db import models

# Create your models here.

class Task(models.Model):
    TODO = 'todo'
    DONE = 'done'

    STATUS_CHOICES = (
        (TODO, 'todo'),
        (DONE, 'done')
    )

    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)

    def __str__(self):
        """Convert obj to str"""
        return self.description