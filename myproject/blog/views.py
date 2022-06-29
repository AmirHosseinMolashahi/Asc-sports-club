from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Article, Author
from .mixins import FieldsMixin, AuthorsAccessMixin
# Create your views here.

class Blog(ListView):
    template_name = 'blog/blog.html'
    queryset = Article.objects.published()
    context_object_name = 'Articles'

class BlogDetail(DetailView):
    template_name = 'blog/blog-detail.html'
    context_object_name = 'Article'
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)


class ArticleList(AuthorsAccessMixin,ListView):
    template_name = 'blog/authors-article-list.html'

    def get_queryset(self):
        top_authors = Author.objects.filter(top_author = True)
        top_authors_list = [item.user for item in top_authors]
        if self.request.user in top_authors_list:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(AuthorsAccessMixin,FieldsMixin, CreateView):
    model = Article
    template_name = "blog/article-create-update.html"
    context_object_name = 'Article'
    success_url = reverse_lazy('blog:blog-list')

class ArticleUpdate(FieldsMixin, UpdateView):
    model = Article
    template_name = "blog/article-create-update.html"
    context_object_name = 'Article'
    success_url = reverse_lazy('blog:blog-list')