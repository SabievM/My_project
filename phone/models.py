from django.db import models



class Brand(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'brands'
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренд'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Цвет')
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'colors'
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


class Phone(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Название телефона')
    brand = models.ForeignKey(to=Brand, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Бренд телефона')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')
    ram = models.IntegerField(default=0, blank=True, null=True, verbose_name='Основная память')
    rom = models.IntegerField(default=0, blank=True, null=True, verbose_name='Оперативная память')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, verbose_name='Цена')
    color = models.ForeignKey(to=Color, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Цвет телефона')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='phones_images', blank=True, null=True, verbose_name='Изображение1')
    image1 = models.ImageField(upload_to='phones_images', blank=True, null=True, verbose_name='Изображение2')
    image2 = models.ImageField(upload_to='phones_images', blank=True, null=True, verbose_name='Изображение3')
    image3 = models.ImageField(upload_to='phones_images', blank=True, null=True, verbose_name='Изображение4')

    class Meta:
        db_table = 'phones'
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
        ordering = ("id",)

    def __str__(self):
        return self.name
    
    def discount_calculation(self):
        return self.price - (self.price * self.discount / 100)
    

