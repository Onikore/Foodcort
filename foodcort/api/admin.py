from django.contrib import admin

from .models import Food, FoodType, Ingredients, Malls, Restaurants, Status, Sales, SaleDetails

myModels = [FoodType, Ingredients,
            Malls, Status]


class SaleItemInline(admin.TabularInline):
    model = SaleDetails
    extra = 0


class SalesAdmin(admin.ModelAdmin):
    inlines = [SaleItemInline]

    class Meta:
        model = Sales


class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'type']

    class Meta:
        model = Food


class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating']

    class Meta:
        model = Restaurants


admin.site.register(myModels)
admin.site.register(Restaurants, RestaurantsAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Sales, SalesAdmin)
