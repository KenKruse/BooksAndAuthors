from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_book', views.create_book),
    path('specific_book_info/<int:book_id>', views.specific_book_info),
    path('/specific_book_info/<int:book_id>/append_authors', views.append_authors),
    path('/authors', views.authors),
    path('/create_author', views.create_author),
    path('/specific_author_info/<int:author_id>', views.specific_author_info),
    path('/specific_author_info/<int:author_id>/append_books', views.append_books),
]