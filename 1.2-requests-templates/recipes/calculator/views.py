from django.shortcuts import render

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
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipes(request, recipe):
    tmp_dict = DATA.get(recipe)
    template = 'calculator/index.html'

    servings = request.GET.get('servings')

    if servings:
        serv_dict = {}
        for k, v in tmp_dict.items():
            serv_dict[k] = round(v*int(servings), 1)

        context = {
            'recipe': serv_dict
        }
    else:

        context = {
            'recipe': tmp_dict
        }
    return render(request, template, context)
