from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #импорт уже готового шаблона авторизации и регистрации
from users.models import User

from django import forms #пакет для стилей формы

class UserLoginForm (AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'введите имя пользователя'
    })) #кастомизируем поля ввода (указываем какой input и подключаем классы из html файла и плэйхолдер (в моем случае только плэйхолдер))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'введите пароль'
    }))

    class Meta:  #класс помогает определить модели с какими полями он будет работать (куда отправлять полученные данные и с чем связывать)
        model = User #в данном случае этот класс будет работать с моделью пользователей (из users.models)
        fields = ('username', 'password') #а конкретно с такими полями

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'введите имя пользователя'
    })) 
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'введите пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'подтвердите пароль'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'введите имя'
    })) 
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'введите фамилию'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : 'введите почту'
    }))
    

    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'username','email','password1', 'password2' )
