from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import LoginUserForm
from main.models import Disciplines, UserDiscipline


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

#class RegisterUser(CreateView):
    #form_class = RegisterUserForm
    #template_name = 'main/register.html'
    #success_url = reverse_lazy('contacts')

    #def form_valid(self, form):
        #user = form.save()
        #login(self.request, user)
        #return redirect('contacts')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('disciplines')


def logout_user(request):
    logout(request)
    return redirect('login')
