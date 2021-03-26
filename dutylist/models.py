from django.db import models
import os
from django import template
# Create your models here.

class Duty(models.Model):
    file = models.FileField(upload_to='duties')
    created = models.DateTimeField(auto_now_add=True)
    

    register = template.Library()

    @register.filter
    def filename(self):
        return os.path.basename(value.file.name)
    def __str__(self):
        return os.path.basename(self.file.name)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)