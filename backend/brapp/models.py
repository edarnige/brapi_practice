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


class Contact(models.Model):
    cropDbId = models.ForeignKey('Crop', on_delete=models.CASCADE, verbose_name=' cropDbId')
    contactDbId = models.TextField(primary_key=True, verbose_name=' contactDbId')
    name = models.TextField(blank=True, verbose_name=' name')
    email = models.TextField(blank=True, verbose_name=' email')
    type = models.TextField(blank=True, verbose_name=' type')
    orcid = models.TextField(blank=True, verbose_name=' orcid')
    instituteName = models.TextField(blank=True, verbose_name=' instituteName')

    def __str__(self):
        return '{}: {}'.format(self.pk, self.name)


class Crop(models.Model):
    cropDbId = models.TextField(primary_key=True, verbose_name=' cropDbId')
    commonName = models.TextField(verbose_name=' commonName')

    def __str__(self):
        return '{}: {}'.format(self.pk, self.commonName)