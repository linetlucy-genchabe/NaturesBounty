from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(Likes)
