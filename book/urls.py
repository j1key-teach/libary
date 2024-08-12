from django.urls import path
from .views import BookListCreateView
from .views import BookRetrieveView, BookUpdateView, BookDeleteView
from .views import BookCreateView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list'),
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('<int:pk>/', BookRetrieveView.as_view(), name='book-detail'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
