
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseNotFound, HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'cake': {
         'сыр сливочный, г': 500,
         'сливки 35%, г': 200,
         'яйца куриные, шт': 4,
         'масло сливочное, г': 100,
         'сахар, ч.л.': 5,
         'лимон (для цедры), шт': 1,
    },
    'pina_colada': {
         'светлого рома, мл': 60,
         'кокосовых сливок, мл':  30,
         'сливок, мл': 30,
         'свежевыжатого ананасового сока, мл': 180,
         'крошеного льда, г': 70,
         'ломтик ананаса с кожурой, шт': 1,
         'красная коктейльная вишня, шт': 1,
         'коктейльная трубочка, шт':  1,
    }
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

#Созданы обработчики под каждое блюдо с возможностью расчета
# количества ингридтентов в зависмости от количества порций
def omlet(request):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get('omlet')
    for x in recipe:
        recipe[x] *= servings
    context = {
        'recipe': DATA.get('omlet'),
    }
    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get('pasta')
    for x in recipe:
        recipe[x] *= servings
    context = {
        'recipe': DATA.get('pasta')
    }
    return render(request, 'calculator/index.html', context)

def butter(request):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get('butter')
    for x in recipe:
          recipe[x] *= servings
    context = {
        'recipe': DATA.get('butter')
    }
    return render(request, 'calculator/index.html', context)

def cake(request):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get('cake')
    for x in recipe:
        recipe[x] *= servings
    context = {
        'recipe': DATA.get('cake')
    }
    return render(request, 'calculator/index.html', context)

def pina_colada(request):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get('pina_colada')
    for x in recipe:
        recipe[x] *= servings
    context = {
        'recipe': DATA.get('pina_colada')
    }
    return render(request,'calculator/index.html', context)





