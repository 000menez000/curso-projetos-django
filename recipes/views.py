from django.shortcuts import render
from utils.recipes.factory import Factory
from .models import Recipe

factory = Factory()

def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })

def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': factory.make_recipe(),
        'is_datail_page': True, 
    })
