from django.contrib import admin

from .models import Food, FoodType, FoodIngredients, Ingredients, Malls, Restaurants, FoodCourts, Status, Roles, Menu, \
    SalesDetails, Sales

myModels = [Food, FoodType, FoodIngredients, Ingredients,
            Malls, Restaurants, FoodCourts, Status, Roles, Menu,
            Sales,SalesDetails]
admin.site.register(myModels)
