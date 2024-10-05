from django.contrib import admin
from basket.models import Basket, BasketLine

class BasketLinetabular(admin.TabularInline):
    model = BasketLine
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_time',)
    inlines = (BasketLinetabular,)

admin.site.register(Basket,BasketAdmin)


