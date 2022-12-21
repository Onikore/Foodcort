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
    name = models.CharField(max_length=50, db_index=True, verbose_name='категория')

    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    type = models.ForeignKey("FoodType", related_name='type', on_delete=models.CASCADE, verbose_name='Категория')
    weight = models.FloatField(verbose_name='Вес')
    calories = models.FloatField(verbose_name='Калорийность')
    proteins = models.FloatField(verbose_name='Белки')
    fats = models.FloatField(verbose_name='Жиры')
    carbohydrates = models.FloatField(verbose_name='Углеводы')
    ingredients = models.ManyToManyField("Ingredients", related_name='ingredients')
    cooking_time = models.FloatField(verbose_name='Время готовки')
    description = models.CharField(max_length=255, verbose_name='Описание')
    food_pic = models.ImageField(upload_to='pictures/', verbose_name='изображение')

    class Meta:
        ordering = ('name',)
        verbose_name = 'блюдо'
        verbose_name_plural = 'блюда'

    def __str__(self):
        return self.name


class Malls(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    lat1 = models.FloatField(verbose_name='Широта 1')
    lon1 = models.FloatField(verbose_name='Долгота 1')
    lat2 = models.FloatField(verbose_name='Широта 2')
    lon2 = models.FloatField(verbose_name='Долгота 2')
    restaurants = models.ManyToManyField('Restaurants', related_name='restaurants')

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
    min_price = models.FloatField(verbose_name='Минимальный чек', default=250.0)
    max_price = models.FloatField(verbose_name='Максимальный чек', default=500.0)
    mall = models.CharField(verbose_name='торговый центр', default='ТЦ Гринвич', max_length=50)
    floor = models.IntegerField(verbose_name='Этаж', default=1)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    rating = models.FloatField(verbose_name='Рейтинг', default=5.0)
    description = models.CharField(max_length=255, verbose_name='Описание', default='', null=True)
    rest_pic = models.ImageField(upload_to='pictures/', verbose_name='изображение', default=' ')
    food = models.ManyToManyField('Food', related_name='food')

    class Meta:
        ordering = ('name',)
        verbose_name = 'ресторан'
        verbose_name_plural = 'рестораны'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name='Статус заказа')

    class Meta:
        ordering = ('name',)
        verbose_name = 'статус заказа'
        verbose_name_plural = 'статусы заказов'

    def __str__(self):
        return self.name


class Sales(models.Model):
    restaurant = models.ForeignKey('Restaurants', on_delete=models.CASCADE, verbose_name='Ресторан')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, verbose_name='Статус')
    deadline = models.FloatField(verbose_name='Дедлайн')
    price = models.FloatField(verbose_name='Цена')
    details = models.ManyToManyField('Food', through='SaleDetails')

    class Meta:
        ordering = ('date_time',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Заказ номер: {self.pk}"


class SaleDetails(models.Model):
    food = models.ForeignKey('Food', on_delete=models.CASCADE, verbose_name='Блюдо')
    sale = models.ForeignKey('Sales', on_delete=models.CASCADE, verbose_name='Заказ')
    amount = models.IntegerField(verbose_name='Количество', default=1)

    class Meta:
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детали заказа'

    def __str__(self):
        return f"{self.sale}, Блюдо: {self.food}, Кол-во: {self.amount}"
