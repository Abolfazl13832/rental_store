from django.contrib import admin
from tools.models import Tool, ToolType, Category, ToolImages

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']

class ToolImageTabular(admin.TabularInline):
    model = ToolImages

class ToolTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
class ToolAdmin(admin.ModelAdmin):
    list_display=['name', 'price_per_day', 'category', 'type']
    list_editable =['price_per_day', 'category', 'type']
    search_fields = ['name', 'category', 'type']
    inlines = [ToolImageTabular]
admin.site.register(Tool, ToolAdmin)
admin.site.register(ToolType,ToolTypeAdmin)
admin.site.register(Category,CategoryAdmin)