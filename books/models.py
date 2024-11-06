from django.db import models
import os
from authors.models import Author
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Book(models.Model):
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)  # Thêm trường PDF
    read_count = models.PositiveIntegerField(default=0)   

    def __str__(self):
        return self.title

    
