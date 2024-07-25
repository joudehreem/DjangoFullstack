from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('books',views.books),
    path('add_book',views.add_book),
    path('registration',views.registration),
    path('login',views.login),
    path('logout',views.logout),
    
    path('books/<int:id>/update',views.form_edit_book),
    path('books/delete',views.remove_book),
    path('books/<int:id>/edit',views.edit_book),
    path('books/<int:id>',views.detail_book),
    path('add_favorite/<int:id>', views.add_favorite),
    path('remove_favorite/<int:id>', views.remove_favorite),    
]
