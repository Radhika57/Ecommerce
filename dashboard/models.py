from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

STOCK_CHOICES = [
    ('In Stock','In Stock'),
    ('Out Of Stock','Out Of Stock'),
]

class MeatCategories(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)

class Meat(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Description = RichTextField()
    Weight = models.CharField(max_length=50,null=True,blank=True)
    PCS = models.PositiveIntegerField()
    Price = models.FloatField()
    Discount = models.FloatField()
    finalPrice = models.FloatField()
    stock = models.CharField(max_length=20,choices=STOCK_CHOICES,default="In Stock",null=True,blank=True)
    Categories = models.ForeignKey(MeatCategories,on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Images/Meat_Image',default="",null=True,blank=True)
    
    def __str__(self):
        return f"{self.Name} ({self.Categories.name})"
    
class FMCGCategories(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)

class FMCGSubCategories(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)   

class FMCGBrand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)  


class FMCG(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Category = models.ForeignKey(FMCGCategories,on_delete=models.CASCADE)
    SubCategory = models.ForeignKey(FMCGSubCategories,on_delete=models.CASCADE)
    Brand = models.ForeignKey(FMCGBrand,on_delete=models.CASCADE)
    Quantity = models.CharField(max_length=50,null=True,blank=True)
    stock = models.CharField(max_length=20,choices=STOCK_CHOICES,default="In Stock",null=True,blank=True)
    ManufactureDate = models.DateTimeField(null=True)
    ExpireDate = models.DateTimeField(null=True)
    Price = models.FloatField()
    Discount = models.FloatField()
    FinalPrice = models.FloatField()
    Description = RichTextField()
    Image1 = models.ImageField(upload_to='Images/FMCG_Image',default="",null=True,blank=True)
    Image2 = models.ImageField(upload_to='Images/FMCG_Image',default="",null=True,blank=True)
    Image3 = models.ImageField(upload_to='Images/FMCG_Image',default="",null=True,blank=True)
    Image4 = models.ImageField(upload_to='Images/FMCG_Image',default="",null=True,blank=True)
    def __str__(self):
        return str(self.Name)     
    
    
class ClothesCategories(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)

class ClothesSubCategories(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)     

class ClothesBrand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)  
    
    
class Clothes(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    MainCategory = models.ForeignKey(ClothesCategories,on_delete=models.CASCADE,null=True)
    SubCategory = models.ForeignKey(ClothesSubCategories,on_delete=models.CASCADE)
    Brand = models.ForeignKey(ClothesBrand,on_delete=models.CASCADE)
    Quantity = models.CharField(max_length=50,null=True,blank=True)
    Color = models.CharField(max_length=20,null=True,blank=True)
    Size = models.CharField(max_length=20,null=True,blank=True)
    Price = models.FloatField()
    Discount = models.FloatField()
    finalprice = models.FloatField()
    stock = models.CharField(max_length=20,choices=STOCK_CHOICES,default="In Stock",null=True,blank=True)
    Description = RichTextField()
    Image1 = models.ImageField(upload_to='Images/Clothes_Image',default="",null=True,blank=True)
    Image2 = models.ImageField(upload_to='Images/Clothes_Image',default="",null=True,blank=True)
    Image3 = models.ImageField(upload_to='Images/Clothes_Image',default="",null=True,blank=True)
    Image4 = models.ImageField(upload_to='Images/Clothes_Image',default="",null=True,blank=True)


    def __str__(self):
        return str(self.Name) 
    
    
class MedicineCategory(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    
    def __str__(self):
        return str(self.name) 
    
class MedicineBrand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)   

class Medicine(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Category = models.ForeignKey(MedicineCategory,on_delete=models.CASCADE)
    Brand = models.ForeignKey(MedicineBrand,on_delete=models.CASCADE)
    Description = RichTextField()
    Quantity = models.CharField(max_length=50,null=True,blank=True)
    ManufactureDate = models.DateField(null=True)
    ExpireDate = models.DateField(null=True)
    Price = models.FloatField()
    Discount = models.FloatField()
    finalprice = models.FloatField()
    Storage = models.CharField(max_length=200,null=True,blank=True)
    Uses = models.CharField(max_length=200,null=True,blank=True)
    Benefits = models.CharField(max_length=200,null=True,blank=True)
    SideEffects = models.CharField(max_length=200,null=True,blank=True)
    How_to_use = models.CharField(max_length=200,null=True,blank=True)
    stock = models.CharField(max_length=20,choices=STOCK_CHOICES,default="In Stock",null=True,blank=True)
    Image1 = models.ImageField(upload_to='Images/Medicine_Image',default="",null=True,blank=True)
    Image2 = models.ImageField(upload_to='Images/Medicine_Image',default="",null=True,blank=True)
    
    def __str__(self):
        return str(self.Name) 
    
    
class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    
    def __str__(self):
        return str(self.id)