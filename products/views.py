from django.shortcuts import render , HttpResponse

from products.models import category, eat, article

# Create your views here
# переменные - контролеры - вьюхи

def index (request):
    context = {
        'title' : 'home' ,
        'article' : article.objects.all(),
        'is_promo': True, #если True то элемент в этом блоке html виден пользователю
        'title' : 'menu',
        'menu' : [
            {
                'name' : 'паста',
                'structure' : 'курица грибы',
            },
            {
                'name' : 'суп',
                'structure' : 'вода картошка',
            },
        ]
         }
    return render (request , 'products/index.html', context)

def menu (request):
    content = {
        'product' : eat.objects.all(),
        'category' : category.objects.all(),
        
    }

    return render (request , 'products/menu.html',content)

def register (request):
    return render (request , 'products/register.html')
