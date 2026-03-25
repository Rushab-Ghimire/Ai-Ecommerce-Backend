from django.db import models
from core.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products'
    )
   

    def __str__(self):
        return self.name
    
class Inventory(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='inventory')
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.stock}"
    

# auto-create inventory when a product is created
@receiver(post_save, sender=Product)
def create_inventory(sender, instance, created, **kwargs):
    if created:
        Inventory.objects.get_or_create(product=instance)