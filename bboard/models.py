from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=50, verbose_name='Produkt')
    content = models.TextField(null=True, blank=True, verbose_name='Opis')
    price = models.FloatField(null=True, blank=True, verbose_name='Cena')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Czas publikacji')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Kategoria')

    class Meta:
        verbose_name_plural = 'Ogłoszenia'
        verbose_name = 'Ogłoszenie'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Kategoria')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Kategorii'
        verbose_name = 'Kategoria'
        ordering = ['name']

