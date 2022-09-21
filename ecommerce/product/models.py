from django.db import models

# Create your models here.
# inherit models
# do not specify primary key
class Product(models.Model):
    name = models.CharField(max_length=50)
    price  = models.FloatField()
    qty = models.IntegerField()
    isAvailable = models.BooleanField()
    detail = models.TextField()
    ratings = models.FloatField()
    shippingCharge = models.FloatField(null=True)
    
    
    class Meta:
        db_table = "products"
    
    def __str__(self):
        return self.name    
    
    
class Tutorial(models.Model):
    tutorial_name = models.CharField(max_length=50)
    tutorial_price = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "tutorials"
        
    def __str__(self):
        return self.tutorial_name    