from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'birth_date', 'nationality', 
                  'profile_picture', 'awards', 'books'] 
