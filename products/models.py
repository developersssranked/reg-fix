from django.db import models
# from firstpr.wsgi import *

# Create your models here
# models = таблицы
# python manage.py makemigrations -для создания миграции всех конструкции

# python manage.py migrate

# про фикстуры он говорил в 5 ролике


# модель категорий:
class category (models.Model):
    name = models.CharField(max_length=128)  #CharField - это строковое поле для строк малого и большого размера (максимум указываем сами)
    description = models.TextField(null=True,blank=True) #ну понятно что то для бол кол-во текста (поле может быть пустым)

    def __str__ (self):
        return self.name #выводим информацию об обьекте в виде названия переданной name (мы переписываем модуль)

class eat (models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField ()
    price = models.DecimalField (max_digits=6, decimal_places=2)#для работы с ценами (сколько цифр до и после запятой)
    quantity = models.PositiveIntegerField(default=0) #кол-во товаров (по умолчанию)
    # image = models.ImageField(upload_to='product_images')для изображений (куда будут сохранятся изображения)
    category = models.ForeignKey(to=category, on_delete=models.CASCADE)#к какой категории относится продукт (связываем нашу модель с другим классом, cascade - предупреждает об удалении всего в категории  protect - не удалит пока категория не будет пустой )

    def __str__ (self):
        return f'продукт : {self.name} | категория : {self.category.name}'

class article (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'image')
    
    def __str__ (self):
        return self.name



# работа с консолью

# (добавление элементов в таблицу):
# from products.models import category
# categorys = category (name = 'одежда', description = 'описание для одежды')
# categorys.save()
# categorys - выведет нам значения этой переменной
# categorys = category.objects.get(id =1) - выводит название обьекта .all - всю бызу данных этого класса
# categorys -не забудь прописать это

# category.objects.create(name = 'лазанья') - один из вариантов добавления (быстрый)
# category.objects.filter(discription = None) - фидьтр обьекты (у которых нет описание в данном случае)'

# всю инфу по shell можно найти загуглив - django all


# выводит список элементов
# from products.models import eat
# eating = eat.objects.all()
# for eat in eating:
#     print(eating)


# выводим фикстуру - она нужна для сохранения базы данных в случае удаления :
# ./manage.py dumpdata products.eat > eatss.json
# создаем папку fixtures в products и перекидываем туда созданные фикстуры
# что бы загрузить все значения базы данных:
# ./manage.py loaddata /путь от firstpr 

