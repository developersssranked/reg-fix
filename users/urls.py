from django.urls import path  
from . import views  #из этой же директории импорт файла views



app_name = 'users'

urlpatterns = [
    path('log/', views.log , name ='log'), 
    path ('reg/', views.reg, name='reg'),
]