from django.db import models

from product.models import Products


# Create your models here.
class Comment(models.Model):
    content = models.TextField(max_length=3000,
                               verbose_name="Comment",
                               help_text="Enter a comment")
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE,
                                null=True)
    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = 'Comments'
