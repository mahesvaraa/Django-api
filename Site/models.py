from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Фото')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Тег')
    title = models.CharField(max_length=255, verbose_name='Название')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def resolution(self):
        return self.photo.width // self.photo.height

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-created_at']