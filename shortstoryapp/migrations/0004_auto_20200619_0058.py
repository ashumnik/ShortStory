# Generated by Django 3.0.7 on 2020-06-18 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortstoryapp', '0003_author_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(upload_to='authors_image/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='author',
            name='url',
            field=models.SlugField(max_length=130, unique=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='illustration',
            field=models.ImageField(upload_to='stories_illustration/', verbose_name='Иллюстрация'),
        ),
    ]
