from django.urls import path
from .views import HomePage,AboutUs

app_name = "home"

urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('about_us/', AboutUs.as_view(), name='about-us'),
]