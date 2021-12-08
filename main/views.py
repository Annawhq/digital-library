from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import LoginUserForm
from main.models import Disciplines, UserDiscipline, Books


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def disciplines(request):
    userid = request.user.id
    discip = UserDiscipline.objects.filter(user=userid)
    return render(request, 'main/disciplines.html', {"discip": discip})


def books(request):
    book = Books.objects.all()
    return render(request, 'main/books.html', {"books": book})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('disciplines')


def logout_user(request):
    logout(request)
    return redirect('login')
