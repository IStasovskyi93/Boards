from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=50, verbose_name='Produkt')
    content = models.TextField(null=True, blank=True, verbose_name='Opis')
    price = models.FloatField(null=True, blank=True, verbose_name='Cena')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Czas publikacji')

    class Meta:
        verbose_name_plural = 'Ogłoszenia'
        verbose_name = 'Ogłoszenie'
        ordering = ['-published']

