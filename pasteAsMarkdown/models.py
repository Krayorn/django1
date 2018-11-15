from django.db import models

# Create your models here.

class Markdown(models.Model):
    markdownText = models.TextField()
    url = models.CharField(max_length=40, unique=True, blank=True)

    def __str__(self):
        return self.markdownText
