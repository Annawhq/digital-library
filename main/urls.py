from django.conf.urls import url
from django.urls import path
from . import views
from .views import LoginUser, logout_user, disciplines, books, search_results, search_book

urlpatterns = [
    path('', views.index, name='home'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('disciplines', views.disciplines, name='disciplines'),
    path('books/<int:pk>/', views.books, name='books'),
    path('search/', search_results, name='search_results'),
    path('searchbook/', search_book, name='search_book'),
]
