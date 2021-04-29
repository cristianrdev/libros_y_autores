from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('new_book', views.save_book),
    path('books/<num>', views.books_detail),
    
    path('authors', views.authors),
    path('new_author', views.save_author),
    path('authors/<num>', views.authors_detail),
    # path('libro_a_autores/<num>', views.asociar_libro_a_autores),
]