from django.db import models

# Create your models here.
class Exercise(models.Model):
    
    name = models.CharField(max_length=50)
    bodyPart = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'createdAt', 'updated']