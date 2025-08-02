from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
   list_display = ['name', 'category', 'price']
   list_filter = ['category']
   search_fields = ['name', 'description']
   prepopulated_fields = {'slug': ('name', )}


class CategoryAdmin(admin.ModelAdmin):
   list_display = ['name', 'slug']
   prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
