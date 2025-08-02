from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.name)
       super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Product(models. Model):
   name = models.CharField(verbose_name='Название', max_length=100, unique=True)
   slug = models.CharField(max_length=100, unique=True)
   category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
   description = models.TextField(verbose_name='Описание', blank=True)
   image = models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='products/')
   price = models.DecimalField(verbose_name='Цена', max_digits=7, decimal_places=2, default=0.00)
   discount = models.DecimalField(verbose_name='Скидка', max_digits=7, decimal_places=2, default=0.00)
   quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)

   def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.name)
       super().save(*args, **kwargs)

   def __str__(self):
       return self.name

   def display_id(self):
       return f'{self.id:05}'

   def sell_price(self):
       if self.discount:
           return round(self.price - self.price * self.discount / 100, 2)
       return self.price

   class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
