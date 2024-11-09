from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200, null=True)
    
    #relational fields
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Supplier = models.ManyToManyField(Supplier)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    