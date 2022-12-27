from django.shortcuts import render , HttpResponsePermanentRedirect 
from django.urls import reverse #импортируем реверс и редирект для того что бы перенаправлять пользователя после регистрации

from users.forms import UserLoginForm, UserRegistrationForm #испортируем форму
from django.contrib import auth 


# вход пользователя
def log (request):
    if request.method == 'POST': #если пришел пост запрос
        form = UserLoginForm(data = request.POST) #передаем данные из заполненный форм(из регистрации)
        if form.is_valid(): #проверка правильности данных (валидация)
            username = request.POST['username'] #если прошло валидацию то достаем из пост запроса (он является словарем) логин и пороль
            password = request.POST['password']
            #далее подтверждение. Есть ли такой пользователь в базе данных
            user = auth.authenticate (username = username, password = password) #так выглядит проверка по поролю и логину 
            if user: #если пользователя нашло в бд (то есть он есть)
                auth.login (request, user) #то его авторизует  
                return HttpResponsePermanentRedirect (reverse('products:home'))#перенаправление на главную страницу (так можно вернуть хоть куда)


    else :
        form =  UserLoginForm()
    context = {'form' : form}  #привязали форму к ключу для работы в html шаблоне
    return render (request, 'users/log.html', context)


# регистрация пользователя
def reg (request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save() # после валидации сохраняем его данные в бд
            return HttpResponsePermanentRedirect (reverse('users:log'))
    else:
        form = UserRegistrationForm()
    context = {'form' : form}
    return render (request, 'users/reg.html', context)


# from users.models import User
# User.objects.all() для просмотра всех зареганных юзеров