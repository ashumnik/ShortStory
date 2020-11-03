from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

    path("registration/", views.RegistrationPage, name="registration"),
    path("login/", views.LoginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),

    path("", views.IndexView.as_view()),
    path("about/", views.AboutView.as_view()),
    path("stories/", login_required(views.StoriesView.as_view())),
    path("<slug:slug>/", login_required(views.StoriesDetailView.as_view()), name = "story_detail"),
    path("author/<str:slug>/", login_required(views.AuthorView.as_view()), name = "author"),
    path('like/<str:url>', views.LikeView, name='story_likes'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
