from django.db import models
from dashboard.models import *
from django.contrib.auth.models import User
from Useraccount.models import User

# Create your models here.

class MeatReview(models.Model):
    meat = models.ForeignKey(Meat, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    review = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.meat)
    
    
class FMCGReview(models.Model):
    fmcg = models.ForeignKey(FMCG, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    review = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.fmcg)
    
class ClothesReview(models.Model):
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    review = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.clothes)
    
class MedicineReview(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    review = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.medicine)
    