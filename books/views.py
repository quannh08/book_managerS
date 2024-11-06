from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Phương thức để tăng số lần đọc khi nhận request PATCH
    @action(detail=True, methods=['patch'], url_path='increase-read-count')
    def increase_read_count(self, request, pk=None):
        # Lấy đối tượng sách theo primary key (pk)
        instance = self.get_object()
        # Tăng số lần đọc thêm 1
        instance.read_count += 1
        instance.save()  # Lưu thay đổi vào cơ sở dữ liệu
        # Trả về kết quả sau khi cập nhật
        return Response(
            {"status": "Read count increased", "read_count": instance.read_count},
            status=status.HTTP_200_OK
        )

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


