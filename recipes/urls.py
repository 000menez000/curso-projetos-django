from django.urls import path
from recipes.views import recipes, about, contact

urlpatterns = [
    path('', recipes),
    path('sobre/', about),
    path('contato/', contact),
]
