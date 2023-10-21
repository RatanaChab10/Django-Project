from django.db import models
import datetime 
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    objects = models.Manager()
    name=models.CharField(max_length=20,unique=True,null=True,blank=True)
    create_by=models.IntegerField(null=True,blank=True)
    update_date=models.IntegerField(null=True,blank=True)
    create_date=models.DateTimeField(default=datetime.datetime.now)
    update_date=models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    objects = models.Manager()
    name=models.CharField(max_length=20,unique=True,null=True,blank=True)
    barcode=models.BigIntegerField(null=True,unique=True)
    unitprice=models.FloatField()
    qtyInstock=models.IntegerField()
    photo=models.ImageField(upload_to="media/",null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='Category')
    create_by=models.IntegerField(null=True,blank=True)
    update_date=models.IntegerField(null=True,blank=True)
    create_date=models.DateTimeField(auto_now_add=datetime.datetime.now)
    update_date=models.DateTimeField(null=True,blank=True)
    
    
    def __str__(self):
        return self.name
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile',on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg",upload_to='profile/')
    
    def __str__(self):
        return f'{self.user.username} UserProfile'
        