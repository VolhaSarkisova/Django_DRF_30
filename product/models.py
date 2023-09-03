from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Name",
                            help_text="Enter the category name")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

class Products(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Name",
                            help_text="Enter the product name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Products'
