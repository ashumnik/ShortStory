from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .models import Story, Author
from .forms import CreateUserForm

def LikeView(request, url):
    story = get_object_or_404(Story, id=request.POST.get('story_id'))
    liked = False
    if story.likes.filter(id=request.user.id).exists():
        story.likes.remove(request.user)
        liked = False
    else:
        story.likes.add(request.user)
        liked = True

    data = {
        'value': liked,
        'likes': story.total_likes()
    }

    return JsonResponse(data, safe=False)

    return HttpResponseRedirect(reverse('story_detail', args=[str(url)]))

class IndexView(View):
    """Главная страница"""
    def get(self, request):
        stories = Story.objects.all();
        return render(request, "shortstoryapp/index.html", {"index": stories})

class StoriesView(ListView):
    """Список рассказов"""
    model = Story
    queryset = Story.objects.filter(draft=False)

class StoriesDetailView(DetailView):
    """Детальное описние рассказа"""
    model = Story
    slug_field = "url"

    def get_context_data(self, *args, **kwargs):
        stuff = get_object_or_404(Story, id=self.object.pk)
        total_likes = stuff.total_likes()
        context = super(StoriesDetailView, self).get_context_data()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AboutView(TemplateView):
    """О нас"""
    template_name = "shortstoryapp/about.html"

def LoginPage(request):
    """Вход"""
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Неправильное имя пользователя ИЛИ пароль')

    context = {}
    return render(request, "shortstoryapp/login.html", context)

def RegistrationPage(request):
    """Регистрация"""
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Был создан аккаунт для ' + user)

                return redirect('login')

    context = {'form':form}
    return render(request, 'shortstoryapp/registration.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

class AuthorView(DetailView):
    """Вывод информации о писателе"""
    model = Author
    template_name = 'shortstoryapp/author.html'
    slug_field = "url"
