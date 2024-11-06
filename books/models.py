from django.db import models
import os
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    description = models.TextField()
    content = models.FileField(upload_to='pdfs/', null=True, blank=True)
    image = models.URLField()
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)  # Thêm trường PDF
    read_count = models.PositiveIntegerField(default=0)   

    def __str__(self):
        return self.title

    
