from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CategoryViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
