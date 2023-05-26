from django.contrib import admin
from .models import *
# Register your models here.
class MeatReviewAdmin(admin.ModelAdmin):
    list_display=['meat','name','rating','review']   
    
class FMCGReviewAdmin(admin.ModelAdmin):
    list_display=['fmcg','name','rating','review']  
    
class ClothesReviewAdmin(admin.ModelAdmin):
    list_display=['clothes','name','rating','review']  
    
class MedicineReviewAdmin(admin.ModelAdmin):
    list_display=['medicine','name','rating','review']
      
    
admin.site.register(MeatReview,MeatReviewAdmin)
admin.site.register(FMCGReview,FMCGReviewAdmin)
admin.site.register(ClothesReview,ClothesReviewAdmin)
admin.site.register(MedicineReview,MedicineReviewAdmin)