from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class MeatCategoriesForm(forms.ModelForm):
    class Meta:
        model = MeatCategories
        fields = '__all__'
    
class MeatForm(forms.ModelForm):
    class Meta:
        model = Meat
        fields = '__all__'
        Description = forms.CharField(widget=CKEditorWidget())
        
class FMCGCategoryForm(forms.ModelForm):
    class Meta:
        model = FMCGCategories
        fields = '__all__'
        
class FMCGSubCategoryForm(forms.ModelForm):
    class Meta:
        model = FMCGSubCategories
        fields = '__all__'
        
class FMCGBrandForm(forms.ModelForm):
    class Meta:
        model = FMCGBrand
        fields = '__all__'
        
        
class FMCGForm(forms.ModelForm):
    class Meta:
        model = FMCG
        fields = '__all__'
        
class ClothesCategoriesForm(forms.ModelForm):
    class Meta:
        model = ClothesCategories
        fields = '__all__'
        
class ClothesSubCategoriesForm(forms.ModelForm):
    class Meta:
        model = ClothesSubCategories
        fields = '__all__'
        
class ClothesBrandForm(forms.ModelForm):
    class Meta:
        model = ClothesBrand
        fields = '__all__'
        
class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = '__all__'  
        
        
class MedicineCategoryForm(forms.ModelForm):
    class Meta:
        model = MedicineCategory
        fields = '__all__'
        
class MedicineBrandForm(forms.ModelForm):
    class Meta:
        model = MedicineBrand
        fields = '__all__'
        
class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'   


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'




