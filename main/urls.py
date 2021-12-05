from django.urls import path
from . import views
from .views import LoginUser, logout_user, disciplines

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('disciplines', disciplines, name='disciplines'),
]
