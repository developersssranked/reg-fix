from django.urls import path  
from . import views  #из этой же директории импорт файла views

# from django.conf.urls.static import static
# from django.conf import settings

app_name = 'products'

urlpatterns = [
    path('', views.index , name ='home'), 
    path('my menu', views.menu , name = 'menu'), 
    path ("your register", views.register, name= 'register'),
]

# if settings.DEBUG:
#     urlpatterns == static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

