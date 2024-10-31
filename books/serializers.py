from rest_framework import serializers
from .models import Book, Category, Author

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [ 'name','id' ]
        
class BookSerializer(serializers.ModelSerializer):
    ID_category = CategorySerializer()
    id_author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'ID_category', 'id_author', 'title', 'description', 'content', 'image']
