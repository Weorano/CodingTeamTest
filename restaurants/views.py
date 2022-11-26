from django.db.models import Count, Case, When, IntegerField, Prefetch
from rest_framework import generics

from restaurants.models import FoodCategory, Food
from restaurants.serializers import FoodListSerializer


class FoodList(generics.ListAPIView):
    """
    Просмотр списка всех блюд для раздела меню в системе.

    """

    queryset = FoodCategory.objects.annotate(
        num_published=Count(Case(
            When(food__is_publish=True, then=1),
            output_field=IntegerField(),
        ))
    ).filter(num_published__gt=0).prefetch_related(
        Prefetch("food", queryset=Food.objects.filter(is_publish=True))
    )

    serializer_class = FoodListSerializer
