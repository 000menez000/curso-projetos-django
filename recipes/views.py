from django.shortcuts import render
from utils.recipes.factory import Factory

factory = Factory()

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [factory.make_recipe() for _ in range(10)]
    })

def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': factory.make_recipe(),
        'is_datail_page': True, 
    })
