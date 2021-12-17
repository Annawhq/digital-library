from django.conf.urls import url
from django.urls import path
from . import views
from .views import LoginUser, logout_user, disciplines, books

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('disciplines', views.disciplines, name='disciplines'),
    path('books/<int:pk>/', views.books, name='books'),
]
