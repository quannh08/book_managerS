from rest_framework import serializers
from .models import ReadHistory

class ReadHistorySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='id_user.username')
    id_book = serializers.CharField(source='id_book.id_book')
    class Meta:
        model = ReadHistory
        fields = ("username", "id_book", "read_at")