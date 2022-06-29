from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Article


class HomePage(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage,self).get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(status = 'p' ,is_special = True)[:4]
        return context


class AboutUs(TemplateView):
    template_name = 'home/about_us.html'