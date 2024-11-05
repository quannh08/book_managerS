from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def partial_update(self, request, *args, **kwargs):
        # Lấy đối tượng book theo primary key (pk)
        instance = self.get_object()
        # Nếu có tham số 'read_count' trong request, cập nhật số lần đọc
        if 'read_count' in request.data:
            try:
                # Tăng số lần đọc bằng giá trị read_count gửi lên
                instance.read_count += int(request.data['read_count'])
                instance.save()  # Lưu thay đổi vào cơ sở dữ liệu
                return Response({"status": "read_count updated", "read_count": instance.read_count}, status=status.HTTP_200_OK)
            except ValueError:
                return Response({"error": "Invalid read_count value"}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().partial_update(request, *args, **kwargs)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


