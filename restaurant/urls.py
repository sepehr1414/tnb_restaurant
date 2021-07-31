from django.urls import path

from restaurant.views import ListRestaurant,best_food, restaurant_detail, search_restaurant

app_name = 'restaurant'

urlpatterns = [
    path('', ListRestaurant.as_view(), name='list_restaurant'),
    path('restaurant/<slug:slug>/', restaurant_detail, name='detail_restaurant'),
    path('food/<slug>/', best_food, name='best_food'),
    path('search/', search_restaurant, name='search_restaurant'),
]

