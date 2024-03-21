from django.urls import path
from . import views as vw

urlpatterns = [
    path('books/', vw.BookListView.as_view(), name='books'),
    path('books/create/', vw.BookCreateView.as_view(), name='book_create'),
    path('books/update/<int:pk>/', vw.BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', vw.BookDeleteView.as_view(), name='book_delete'),
    path('authors/', vw.AuthorListView.as_view(), name='authors'),
    path('authors/create/', vw.AuthorCreateView.as_view(), name='author_create'),
    path('authors/update/<int:pk>/', vw.AuthorUpdateView.as_view(), name='author_update'),
    path('authors/delete/<int:pk>/', vw.AuthorDeleteView.as_view(), name='author_delete'),
    path('genders/', vw.GenderListView.as_view(), name='genders'),
    path('genders/create/', vw.GenderCreateView.as_view(), name='gender_create'),
    path('genders/update/<int:pk>/', vw.GenderUpdateView.as_view(), name='gender_update'),
    path('genders/delete/<int:pk>/', vw.GenderDeleteView.as_view(), name='gender_delete'),
]