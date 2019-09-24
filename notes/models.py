from django.db import models
from django.utils import timezone
# Create your models here.
class Note(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name_plural = 'notes'