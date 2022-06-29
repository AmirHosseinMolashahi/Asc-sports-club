from django.urls import path
from .views import ArticleList, ArticleCreate, ArticleUpdate, Blog , BlogDetail

app_name = "blog"

urlpatterns = [
    path('', Blog.as_view(), name='blog-page'),
    path('posts/<slug:slug>/', BlogDetail.as_view(), name='blog-detail'),

    path('blog_list/',ArticleList.as_view(), name='blog-list'),
    path('create/',ArticleCreate.as_view(), name='article-create'),
    path('update/<slug:slug>/',ArticleUpdate.as_view(), name='article-update'),
]