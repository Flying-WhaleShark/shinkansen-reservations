# reservation/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('check/', views.check, name='check'),
    path('cancel/', views.cancel, name='cancel'),
    path('mypage/', views.mypage, name='mypage'),
]