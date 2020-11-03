# Generated by Django 3.0.7 on 2020-06-18 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='authors/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Писатель',
                'verbose_name_plural': 'Писатели',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Жанр')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Содержание')),
                ('illustration', models.ImageField(upload_to='stories/', verbose_name='Иллюстрация')),
                ('publication_date', models.DateField(default=2019, verbose_name='Дата издания')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortstoryapp.Author', verbose_name='Автор')),
                ('genres', models.ManyToManyField(to='shortstoryapp.Genre', verbose_name='жанры')),
            ],
            options={
                'verbose_name': 'Рассказ',
                'verbose_name_plural': 'Рассказы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortstoryapp.RatingStar', verbose_name='Звезда')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortstoryapp.Story', verbose_name='Рассказ')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
    ]