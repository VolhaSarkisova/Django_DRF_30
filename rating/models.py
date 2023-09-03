from django.db import models

from product.models import Products

# Create your models here.
CHOICES_VALUE = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
)
class Rating(models.Model):
    value = models.IntegerField(choices=CHOICES_VALUE, default=1)
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE,
                                null=True)

    class Meta:
        ordering = ('value',)
        verbose_name_plural = 'Ratings'
