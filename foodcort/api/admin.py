from django.contrib import admin

from .models import Food, FoodType, Ingredients, Malls, Restaurants, Status, \
    SalesDetails, Sales

myModels = [Food, FoodType, Ingredients,
            Malls, Restaurants, Status,
            Sales, SalesDetails]
admin.site.register(myModels)
