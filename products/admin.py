from django.contrib import admin


from .models import eat, category,article


# регитрация своих можделей что бы они отоброжались
admin.site.register(eat)
admin.site.register(category)
admin.site.register(article)