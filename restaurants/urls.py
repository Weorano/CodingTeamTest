from django.urls import path

from restaurants.views import FoodList

urlpatterns = [
    path('', FoodList.as_view(), name="Генерация списка блюд"),
]
