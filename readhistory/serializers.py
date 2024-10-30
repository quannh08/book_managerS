from rest_framework import serializers
from .models import ReadHistory
from books.serializers import BookSerializer


class ReadHistorySerializer(serializers.ModelSerializer):
    # book_title = serializers.CharField(source='id_book.tieu_de')  # Tiêu đề sách
    # book_image = serializers.ImageField(source='id_book.image')  # Hình ảnh sách
    username = serializers.CharField(source='id_user.username')  # Tên người dùng
    book = BookSerializer(source='id_book')
    class Meta:
        model = ReadHistory
        fields = ("username", "book", "read_at")