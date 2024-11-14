from django.shortcuts import render
import jwt
from rest_framework import status
from rest_framework.response import Response
from .models import ReadHistory, Book
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from .models import User

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token:
            raise exceptions.AuthenticationFailed('Token missing')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user = User.objects.get(id=payload['id'])
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            raise exceptions.AuthenticationFailed('Invalid token or token has expired')
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not found')

        return (user, None)

class ReadHistoryAPIView(APIView):
    authentication_classes = [JWTAuthentication]  # Sử dụng lớp JWTAuthentication cho việc xác thực

    def post(self, request, *args, **kwargs):
        user = request.user  # Sau khi xác thực, request.user sẽ là user từ token

        id_book = request.data.get('id')  # Lấy ID của cuốn sách từ dữ liệu gửi lên

        if not id_book:
            return Response({'error': 'id_book không được cung cấp.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Kiểm tra xem cuốn sách có tồn tại không
            book = Book.objects.get(id=id_book)
        except Book.DoesNotExist:
            return Response({'error': 'Cuốn sách không tồn tại.'}, status=status.HTTP_404_NOT_FOUND)

        # Xóa lịch sử đọc cũ nếu tồn tại
        ReadHistory.objects.filter(id_user=user, id_book=book).delete()

        # Tạo bản ghi lịch sử đọc mới
        new_history = ReadHistory.objects.create(id_book=book, id_user=user)

        return Response({'message': 'Đã cập nhật lịch sử đọc!', 'read_at': new_history.read_at}, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        user = request.user  # Sau khi xác thực, request.user sẽ là user từ token

        # Lấy danh sách lịch sử đọc của người dùng
        user_histories = ReadHistory.objects.filter(id_user=user)

        # Chuẩn bị dữ liệu trả về
        read_books = [{"id_book": history.id_book.id, "read_at": history.read_at} for history in user_histories]

        response_data = {
            "username": user.username,
            "read_books": read_books
        }

        return Response(response_data, status=status.HTTP_200_OK)

