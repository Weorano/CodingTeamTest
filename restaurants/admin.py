from django.contrib import admin

from restaurants.models import FoodCategory, Food


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ru', )
    ordering = ('order_id', )


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('code', 'name_ru', 'cost')
    search_fields = ('name_ru', )
    list_filter = ('category', )
