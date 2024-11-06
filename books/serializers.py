from rest_framework import serializers
from .models import Book, Category
import os

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
     
class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = ['id', 'category','authors', 'title', 'description', 'content', 'image','pdf_file','read_count']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['pdf_file'] = os.path.basename(representation['pdf_file'])
        representation['content'] = os.path.basename(representation['content'])
        return representation
    def get_pdf_url(self, obj):
        # Trả về URL đầy đủ của file PDF
        return obj.pdf_file.url if obj.pdf_file else None
