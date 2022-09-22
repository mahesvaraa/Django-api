from django.db.models import F, Q
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Category, Post, Tag


class Home(ListView):
    model = Post
    template_name = 'news/pages/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Original'
        return context


class PostsByCategory(ListView):
    template_name = 'news/pages/category.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class PostsByTag(ListView):
    template_name = 'news/pages/tag.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тегу: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'news/pages/single-post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class Search(ListView):
    template_name = 'news/pages/search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        result_title = Q(title__icontains=self.request.GET.get('search'))
        result_content = Q(content__icontains=self.request.GET.get('search'))

        if result_title or result_content:
            return Post.objects.filter(result_title | result_content)
        else:
            return []

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"search={self.request.GET.get('search')}&"
        return context


# Create your views here.
def index(request):
    return render(request, 'news/pages/index.html')


def contact(request):
    return render(request, 'news/pages/contact.html')


def coming_soon(request):
    return render(request, 'news/pages/coming-soon.html')


def about(request):
    return render(request, 'news/pages/about-us.html')

