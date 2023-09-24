from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('detail/<int:pk>/<str:name>', BookDetailView.as_view(), name='book-detail')
]