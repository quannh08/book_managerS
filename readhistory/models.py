from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User
from books.models import Book
# Create your models here.

class ReadHistory(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    read_at = models.DateTimeField(auto_now_add=True)  # Thời gian đọc sách
    class Meta:
        ordering = ['-read_at']  # Sắp xếp lịch sử theo thời gian mới nhất
    def __str__(self):
        return f"{self.id_user} đọc {self.id_book} lúc {self.read_at.strftime('%Y-%m-%d %H:%M:%S')}"