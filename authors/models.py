from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)  
    birth_date = models.DateField(null=True, blank=True)  
    nationality = models.CharField(max_length=100, null=True, blank=True)  
    profile_picture = models.ImageField(upload_to='authors/', null=True, blank=True) 
    awards = models.TextField(blank=True, null=True)  
    books = models.JSONField(blank=True, null=True)  

    def __str__(self):
        return self.name
