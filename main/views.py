from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

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


def books(request, pk):
    book = Books.objects.filter(discipline=pk)
    return render(request, 'main/books.html', {"book": book})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('disciplines')


def logout_user(request):
    logout(request)
    return redirect('login')


def search_results(request):
    userid = request.user.id
    query = request.GET.get('q')
    object_list = UserDiscipline.objects.filter(
            Q(user=userid) & Q(discip__name__icontains=query)
        )
    return render(request, 'main/search_results.html', {'object_list': object_list})

#class SearchResultsView(ListView):
    #model = Disciplines
    #template_name = 'main/search_results.html'

    #def get_queryset(self):
        #query = self.request.GET.get('q')
        #object_list = Disciplines.objects.filter(name__icontains=query)
        #return object_list
