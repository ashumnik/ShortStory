from django.db import models
from django.urls import reverse
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Genre(models.Model):
    """Жанры"""
    name            = models.CharField("Жанр", max_length=150)
    description     = models.TextField("Описание")
    url             = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Author(models.Model):
    """Писатели (авторы)"""
    name            = models.CharField("Имя", max_length=100)
    description     = models.TextField("Описание")
    image           = models.ImageField("Изображение", upload_to="authors_image/")
    url             = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Писатель"
        verbose_name_plural = "Писатели"

class Story(models.Model):
    """Рассказ"""
    title            = models.CharField("Название", max_length=100)
    description      = models.TextField("Содержание")
    illustration     = models.ImageField("Иллюстрация", upload_to="stories_illustration/")
    author           = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    genres           = models.ManyToManyField(Genre, verbose_name="жанры")
    publication_date = models.DateField("Дата издания", default=2019)
    url              = models.SlugField(max_length=130, unique=True)
    draft            = models.BooleanField("Черновик", default=False)
    likes            = models.ManyToManyField(User, related_name="story_likes")

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count() 

    def get_absolute_url(self):
        return reverse("story_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Рассказ"
        verbose_name_plural = "Рассказы"
