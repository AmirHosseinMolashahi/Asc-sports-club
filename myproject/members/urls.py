from django.urls import path
from .views import CoachesList, TopAthleteList

app_name = "members"

urlpatterns = [
    path('coaches/',CoachesList.as_view(), name="coaches-list"),
    path('top_athlete/',TopAthleteList.as_view(), name="top-athlete-list"),
]