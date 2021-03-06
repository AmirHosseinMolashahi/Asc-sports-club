from pyexpat import model
from django.db import models
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# my manager
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="نویسنده")
    top_author = models.BooleanField(default=False, verbose_name="نویسنده ارشد")

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"
    
    def __str__(self):
        return self.user.get_full_name()


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'), #draft
        ('p', 'منتشر شده'), #publish
        ('i', 'ذر حال بررسی'), #investigation
        ('b', 'برگشت داده شده'), #back
    )
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name="articles", verbose_name="نویسنده")
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی", related_name="articles")
    description = models.TextField(verbose_name="محتوا")
    image = models.ImageField(upload_to="blog/images", verbose_name="تصویر مقاله")
    published = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_special = models.BooleanField(default=False, verbose_name="مقاله ویژه")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-published']


    def __str__(self):
        return self.title
    
    """def jpublished(self):
        return jalali_converter(self.published)
    jpublished.short_description = "زمان انتشار"
"""
    
    def thumnail_tag(self):
        return format_html("<img width=100 height=100 style='border-radius: 100%;' src='{}'>".format(self.image.url))
    thumnail_tag.short_description = "عکس"

    def category_to_str(self):
        return ", ".join([category.title for category in self.category.active()])
    category_to_str.short_description = "دسته بندی"
    
    objects = ArticleManager()