from django.db import models

class Article(models.Model):
    title=models.TextField()
    content=models.TextField()

# Create your models here.
