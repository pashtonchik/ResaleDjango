from django.db import models


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    image = models.ImageField(blank=True)
    size = models.CharField(max_length=30, verbose_name='Размер')
    contact = models.URLField(max_length=100)
    in_progress = models.BooleanField(default=False, verbose_name='Заказ взят в работу')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')

    def __str__(self):
        return f"Заказ {self.id}"

