from django.contrib.auth.models import User
from django.db import models


class Ingredients(models.Model):
    name = models.CharField(max_length=50, verbose_name='ингредиент')

    class Meta:
        ordering = ('name',)
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'

    def __str__(self):
        return self.name


class FoodType(models.Model):
    name = models.CharField(max_length=50, verbose_name='категория')

    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    type = models.ForeignKey("FoodType", on_delete=models.CASCADE, verbose_name='Категория')
    calories = models.FloatField(verbose_name='Калорийность')
    cooking_time = models.FloatField(verbose_name='Время готовки')
    img_path = models.CharField(max_length=255, verbose_name='Путь до изображения')

    class Meta:
        ordering = ('name',)
        verbose_name = 'блюдо'
        verbose_name_plural = 'блюда'

    def __str__(self):
        return self.name


class FoodIngredients(models.Model):
    food = models.ForeignKey("Food", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredients", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'состав блюда'


class Malls(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    lat1 = models.FloatField(verbose_name='Широта 1')
    lon1 = models.FloatField(verbose_name='Долгота 1')
    lat2 = models.FloatField(verbose_name='Широта 2')
    lon2 = models.FloatField(verbose_name='Долгота 2')

    class Meta:
        ordering = ('name',)
        verbose_name = 'торговый центр'
        verbose_name_plural = 'торговые центры'

    def __str__(self):
        return self.name


class Restaurants(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    opening = models.TimeField(verbose_name='Время открытия')
    closing = models.TimeField(verbose_name='Время закрытия')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    class Meta:
        ordering = ('name',)
        verbose_name = 'ресторан'
        verbose_name_plural = 'рестораны'

    def __str__(self):
        return self.name


class FoodCourts(models.Model):
    mall = models.ForeignKey('Malls', on_delete=models.CASCADE, verbose_name='Торговый центр')
    restaurant = models.ForeignKey('Restaurants', on_delete=models.CASCADE, verbose_name='Ресторан')
    floor = models.IntegerField(verbose_name='Этаж')

    class Meta:
        verbose_name = 'фудкорт'
        verbose_name_plural = 'фудкорты'

    def __str__(self):
        return f'{self.mall_id} {self.restaurant_id} {self.floor}'


class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name='Статус заказа')

    class Meta:
        ordering = ('name',)
        verbose_name = 'статус заказа'
        verbose_name_plural = 'статусы заказов'

    def __str__(self):
        return self.name


class Roles(models.Model):
    name = models.CharField(max_length=50, verbose_name='Роль пользователя')

    class Meta:
        ordering = ('name',)
        verbose_name = 'роль'
        verbose_name_plural = 'роли'

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey('Restaurants', on_delete=models.CASCADE, verbose_name='Ресторан')
    food = models.ForeignKey('Food', on_delete=models.CASCADE, verbose_name='Блюдо')

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'

    def __str__(self):
        return f'{self.restaurant_id} {self.food_id}'


class Sales(models.Model):
    restaurant = models.ForeignKey('Restaurants', on_delete=models.CASCADE, verbose_name='Ресторан')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, verbose_name='Статус')
    deadline = models.FloatField(verbose_name='Дедлайн')
    price = models.FloatField(verbose_name='Цена')

    class Meta:
        ordering = ('date_time',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class SalesDetails(models.Model):
    sale = models.ForeignKey('Sales', on_delete=models.CASCADE, verbose_name='Заказ')
    food = models.ForeignKey('Food', on_delete=models.CASCADE, verbose_name='Блюдо')
    portion_count = models.IntegerField(verbose_name='Количество порций')

    class Meta:
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детали заказов'
