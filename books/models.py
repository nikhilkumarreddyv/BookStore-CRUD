from django.db import models

# Create your models here.

class Book(models.Model):
    book_name=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    book_year=models.IntegerField()
    book_image=models.ImageField(upload_to='images')