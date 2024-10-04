from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=255) 
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)
        
    def __str__(self):
        return self.name 

class Item (models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='item_images',)
    
   
    ordering = ('name',)
    def __str__(self):
        return self.name
    