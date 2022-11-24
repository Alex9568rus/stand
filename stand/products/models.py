from django.db import models
from django.urls import reverse


class Tag(models.Model):
    """Тег для обозначения вида ИЗДЕЛИЯ (торт, капкейк и т.д)."""
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название тега'  # название изделия: торт, капкейк и т.д
    )
    slug = models.SlugField(
        verbose_name='Слаг тега',
        unique=True
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name', )

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    def __str__(self):
        return self.name


class Product(models.Model):
    """Готовое изделие (торт, кекс, рулет и т.д) или рецепт."""
    name = models.CharField(
        max_length=200,
        verbose_name='Название изделия',
    )
    tag = models.ForeignKey(
        Tag,
        related_name='tags',
        on_delete=models.SET_NULL,
        verbose_name='Теги',
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Фото готового изделия',
        upload_to='products/cakes/',
    )
    description = models.TextField(
        verbose_name='Описание изделия',
    )
    limits = models.TextField(
        verbose_name='Дополнение',
        blank=True
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )
    extra_price = models.PositiveIntegerField(
        verbose_name='Дополнитьельная цена',
        blank=True,
        default=0
    )
    measurement_unit = models.CharField(
        max_length=100,
        verbose_name='Единица изделия'
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class ExtraPhotos(models.Model):
    photo = models.ImageField(
        verbose_name='Дополнительные фото',
        upload_to='products/extra'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='extra_photos',
        verbose_name='Продукт'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Дополнительное фото'
        verbose_name_plural = 'Дополнительные фото'


class Works(models.Model):
    tag = models.ForeignKey(
        Tag,
        related_name='works',
        on_delete=models.SET_NULL,
        verbose_name='Теги',
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Фото работы',
        upload_to='products/works'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Моя работа'
        verbose_name_plural = 'Мои работы'
