from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60)

class VariantCategory(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, default=None, null=True)
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)

class Variant(models.Model):
    variant_category = models.ForeignKey(VariantCategory, related_name='variant_category' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='variants/', verbose_name='Imagen', null=True, blank=True)
    
    