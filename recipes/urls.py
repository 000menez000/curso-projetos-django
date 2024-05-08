from django.urls import path
from recipes.views import recipes

urlpatterns = [
    path('', recipes),
]
