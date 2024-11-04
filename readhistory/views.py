from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from books.models import Book
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics


# Create your views here.
class ReadHistoryAPIView(generics.ListCreateAPIView):
    queryset = ReadHistory.objects.all()
    serializer_class = ReadHistorySerializer

    def post(self, request, *args, **kwargs):
        id_book = request.data.get('id_book')  # Lấy id_book từ dữ liệu gửi lên
        user = request.user
        
        if user.is_anonymous:
            return Response({'error': 'Bạn cần đăng nhập để cập nhật lịch sử đọc.'}, status=status.HTTP_403_FORBIDDEN)
        if not id_book:
            return Response({'error': 'id_book không được cung cấp.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Kiểm tra xem cuốn sách có tồn tại không
            book = Book.objects.get(id_book=id_book)
        except Book.DoesNotExist:
            return Response({'error': 'Cuốn sách không tồn tại.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Xóa lịch sử đọc cũ nếu tồn tại
        ReadHistory.objects.filter(id_user=user, id_book=book).delete()
        
        # Tạo bản ghi lịch sử đọc mới
        new_history = ReadHistory.objects.create(
            id_book=book,
            id_user=user
        )
        return Response({'message': 'Đã cập nhật lịch sử đọc!', 'read_at': new_history.read_at}, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous:
            return Response({'error': 'Bạn cần đăng nhập để xem lịch sử đọc.'}, status=status.HTTP_403_FORBIDDEN)
        
        user_histories = ReadHistory.objects.filter(id_user=user)

        # Tạo dữ liệu phản hồi
        read_books = [{"id_book": history.id_book.id_book, "read_at": history.read_at} for history in user_histories]
        
        response_data = {
            "username": user.username,
            "read_books": read_books
        }

        return Response(response_data, status=status.HTTP_200_OK)
