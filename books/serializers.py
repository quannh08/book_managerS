from rest_framework import serializers
from .models import Book
import os

class BookSerializer(serializers.ModelSerializer):
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'category', 'authors', 'title', 'description', 'image', 'pdf_file', 'read_count', 'pdf_url']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        pdf_file = representation.get('pdf_file')
        
        if pdf_file:
            # Nếu pdf_file không phải là None, lấy tên file
            representation['pdf_file'] = os.path.basename(pdf_file)
        else:
            # Nếu pdf_file là None, gán giá trị None hoặc chuỗi rỗng
            representation['pdf_file'] = None  # hoặc ""

        return representation

    def get_pdf_url(self, obj):
        # Trả về URL đầy đủ của file PDF nếu có
        return obj.pdf_file.url if obj.pdf_file else None
