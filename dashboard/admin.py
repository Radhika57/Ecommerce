from django.contrib import admin
from .models import *
# Register your models here.
class MeatCategoriesAdmin(admin.ModelAdmin):
    list_display=['name']
    
class MeatAdmin(admin.ModelAdmin):
    list_display=['Name','Description','Weight','Categories','Discount','Price']
    
class FMCGCategoriesAdmin(admin.ModelAdmin):
    list_display=['name']
    
class FMCGSubCategoriesAdmin(admin.ModelAdmin):
    list_display=['name']   
    
class FMCGBrandAdmin(admin.ModelAdmin):
    list_display=['name']   

class FMCGAdmin(admin.ModelAdmin):
    list_display=['Name','Category','SubCategory','Quantity','ManufactureDate','ExpireDate','Price','Discount']

class ClothesCategoriesAdmin(admin.ModelAdmin):
    list_display=['name']
    
class ClothesSubCategoriesAdmin(admin.ModelAdmin):
    list_display=['name']  
    
class ClothesBrandAdmin(admin.ModelAdmin):
    list_display=['name']   

class ClothesAdmin(admin.ModelAdmin):
    list_display=['Name','MainCategory','SubCategory','Brand','Quantity','stock']

class MedicineCategoryAdmin(admin.ModelAdmin):
    list_display=['name']  
    
class MedicineBrandAdmin(admin.ModelAdmin):
    list_display=['name']   

class MedicineAdmin(admin.ModelAdmin):
    list_display=['Name','Category','Brand','Quantity','stock','finalprice']

class FAQAdmin(admin.ModelAdmin):
    list_display=['question','answer']
    
admin.site.register(MeatCategories,MeatCategoriesAdmin)
admin.site.register(Meat,MeatAdmin)
admin.site.register(FMCGCategories,FMCGCategoriesAdmin)
admin.site.register(FMCGSubCategories,FMCGSubCategoriesAdmin)
admin.site.register(FMCGBrand,FMCGBrandAdmin)
admin.site.register(FMCG,FMCGAdmin)
admin.site.register(ClothesCategories,ClothesCategoriesAdmin)
admin.site.register(ClothesSubCategories,ClothesSubCategoriesAdmin)
admin.site.register(ClothesBrand,ClothesBrandAdmin)
admin.site.register(Clothes,ClothesAdmin)
admin.site.register(MedicineCategory,MedicineCategoryAdmin)
admin.site.register(MedicineBrand,MedicineBrandAdmin)
admin.site.register(Medicine,MedicineAdmin)
admin.site.register(FAQ,FAQAdmin)