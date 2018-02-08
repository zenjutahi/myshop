from django.contrib import admin
from .models import Category, Product, SeriesList

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'stock', 'available',
					'created', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'stock', 'available']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class SeriesListAdmin(admin.ModelAdmin):
	list_display = ['name', 'seriesSize', 'bookPosition']
	list_filter = ['name', 'bookPosition']
	list_editable = ['seriesSize', 'bookPosition']
admin.site.register(SeriesList, SeriesListAdmin)
