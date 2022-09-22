from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('category/<str:slug>', PostsByCategory.as_view(), name='category'),
    path('coming-soon', coming_soon, name='coming-soon'),
    path('post/<str:slug>', GetPost.as_view(), name='post'),
    path('tag/<str:slug>', PostsByTag.as_view(), name='tag'),
    path('search', Search.as_view(), name='search'),
    #path('category/<str:slug>', get_category, name='category')
]