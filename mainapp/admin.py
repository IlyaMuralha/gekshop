from django.contrib import admin

from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'short_description', 'price', 'quantity')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    # # Запрет на редактирование
    # readonly_fields = ('category', 'short_description')
    ordering = ('name', 'price', 'category')
    search_fields = ('name', 'category__name')
