from django.contrib import admin
from django.urls import path
from data_app import views
from data_app.views import BookListView , BookUpdateView ,BasicUploadView
urlpatterns = [
    path('records/',views.index, name='index'),
    path('upload/',views.upload, name='uplaod'),
    path('class/books/',views.BookListView.as_view(), name='class_book_list'),
    path('class/upload_book/',views.UploadBookView.as_view(), name='class_uplaod_book'),
    path('class/books/<int:pk>/', views.delete_book , name='delete_book'),
    path('class/upload_book/<int:pk>/', views.BookUpdateView.as_view(), name= 'book-update'),
    path('photo_upload/', views.BasicUploadView.as_view(), name='basic_upload'),
    path('register/', views.register, name='register'),
]
