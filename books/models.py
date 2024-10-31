from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
class Book(models.Model):
    ID_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    image = models.URLField()
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
