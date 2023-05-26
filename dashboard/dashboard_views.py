from django.shortcuts import render , redirect
from .forms import *
from django.views.generic import TemplateView,UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.

def dashboard(request):
    return render(request,'dashboard/Dashboard/index8.html')

#######################################################  MEAT  ########################################################


def AddMeatCategories(request):
    form = MeatCategoriesForm()
    if request.method == 'POST':
        form = MeatCategoriesForm(request.POST)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/Meat/addmeatcategories.html', {'error': form.errors})
    return render(request, 'dashboard/Meat/addmeatcategories.html',{'form':form})

def MeatCategorylist(request):
    Meatcategory = MeatCategories.objects.all()
    return render(request,'dashboard/Meat/meatcategorieslist.html',{'Meatcategory':Meatcategory})

class MeatCategoryUpdateView(UpdateView):
    template_name = 'dashboard/Meat/editmeatcategories.html'
    model = MeatCategories
    fields = ['name']
    success_url ="/meatcategorylist/"

def deletemeatcategory(request,id):
    meat = MeatCategories.objects.get(id=id)
    meat.delete()
    return HttpResponseRedirect(reverse('meatcategorylist'))

def AddMeat(request):
    form = MeatForm()
    if request.method == 'POST':
        form = MeatForm(request.POST,request.FILES)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/Meat/addmeat.html', {'error': form.errors})
    return render(request, 'dashboard/Meat/addmeat.html',{'form':form})


def Meatlist(request):
    Meats = Meat.objects.all()
    return render(request,'dashboard/Meat/Meatlist.html',{'Meats':Meats})

class MeatUpdateView(UpdateView):
    template_name = 'dashboard/Meat/editmeat.html'
    model = Meat
    fields = ['Name','Description','Weight','PCS','Price','Discount','Categories','Image']
    success_url ="/meatlist/"

def deletemeat(request,id):
    meat = Meat.objects.get(id=id)
    meat.delete()
    return HttpResponseRedirect(reverse('meatlist'))

######################################################  FMCG   #########################################################


def AddFMCGCategory(request):
    form = FMCGCategoryForm()
    if request.method == 'POST':
        form = FMCGCategoryForm(request.POST)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/FMCG/addfmcgcategory.html', {'error': form.errors})
    return render(request, 'dashboard/FMCG/addfmcgcategory.html',{'form':form})

def FMCGCategorylist(request):
    FMCGCategory = FMCGCategories.objects.all()
    return render(request,'dashboard/FMCG/fmcgcategorylist.html',{'FMCGCategory':FMCGCategory})

def AddFMCGSubCategory(request):
    form = FMCGSubCategoryForm()
    if request.method == 'POST':
        form = FMCGSubCategoryForm(request.POST)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/FMCG/addfmcgsubcategory.html', {'error': form.errors})
    return render(request, 'dashboard/FMCG/addfmcgsubcategory.html',{'form':form})

def FMCGSubCategoryList(request):
    FMCGSubCategory = FMCGSubCategories.objects.all()
    return render(request,'dashboard/FMCG/fmcgsubcategorylist.html',{'FMCGSubCategory':FMCGSubCategory})


def AddFMCGbrand(request):
    form = FMCGBrandForm()
    if request.method == 'POST':
        form = FMCGBrandForm(request.POST)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/FMCG/addfmcgbrand.html', {'error': form.errors})
    return render(request, 'dashboard/FMCG/addfmcgbrand.html',{'form':form})

def FMCGBrandList(request):
    FMCGbrand = FMCGBrand.objects.all()
    return render(request,'dashboard/FMCG/fmcgBrandlist.html',{'FMCGbrand':FMCGbrand})

def AddFMCG(request):
    form = FMCGForm()
    if request.method == 'POST':
        form = FMCGForm(request.POST,request.FILES)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/FMCG/addfmcgproduct.html', {'error': form.errors})
    return render(request, 'dashboard/FMCG/addfmcgproduct.html',{'form':form})

def FMCGlist(request):
    FMCGs = FMCG.objects.all()
    return render(request,'dashboard/FMCG/fmcgproductlist.html',{'FMCGs':FMCGs})


class FMCGCategoryUpdateView(UpdateView):
    template_name = 'dashboard/FMCG/editfmcgcategory.html'
    model = FMCGCategories
    fields = ['name']
    success_url ="/fmcgcategorylist/"

def deletefmcgcategory(request,id):
    fmcgcategory = FMCGCategories.objects.get(id=id)
    fmcgcategory.delete()
    return HttpResponseRedirect(reverse('fmcgcategorylist'))


class FMCGSubCategoryUpdateView(UpdateView):
    template_name = 'dashboard/FMCG/editfmcgsubcategory.html'
    model = FMCGSubCategories
    fields = ['name']
    success_url ="/fmcgsubcategorylist/"

def deletefmcgsubcategory(request,id):
    fmcgsubcategory = FMCGSubCategories.objects.get(id=id)
    fmcgsubcategory.delete()
    return HttpResponseRedirect(reverse('fmcgsubcategorylist'))

class FMCGBrandUpdateView(UpdateView):
    template_name = 'dashboard/FMCG/editfmcgbrand.html'
    model = FMCGBrand
    fields = ['name']
    success_url ="/fmcgbrandlist/"

def deletefmcgBrand(request,id):
    fmcgbrand = FMCGBrand.objects.get(id=id)
    fmcgbrand.delete()
    return HttpResponseRedirect(reverse('fmcgbrandlist'))

class FMCGUpdateView(UpdateView):
    template_name = 'dashboard/FMCG/editfmcg.html'
    model = FMCG
    fields = ['Name','Category','SubCategory','Quantity','ManufactureDate','ExpireDate','Price','Discount','Description','Image1','Image2','Image3']
    success_url ="/fmcglist/"

def deletefmcg(request,id):
    fmcg = FMCG.objects.get(id=id)
    fmcg.delete()
    return HttpResponseRedirect(reverse('fmcglist'))


########################################################  Clothes  #######################################################

def AddClothesCategories(request):
    form = ClothesCategoriesForm()
    if request.method == 'POST':
        form = ClothesCategoriesForm(request.POST,request.FILES)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/Clothes/addcategory.html', {'error': form.errors})
    return render(request, 'dashboard/Clothes/addcategory.html',{'form':form})

def ClothesCategorieslist(request):
    Category = ClothesCategories.objects.all()
    return render(request,'dashboard/Clothes/clothescategorylist.html',{'Category':Category})

class ClothesCategoriesUpdateView(UpdateView):
    template_name = 'dashboard/Clothes/editcategory.html'
    model = ClothesCategories
    fields = ['name']
    success_url ="/clothescategorylist/"

def deleteClothesCategories(request,id):
    clothescategorylist = ClothesCategories.objects.get(id=id)
    clothescategorylist.delete()
    return HttpResponseRedirect(reverse('clothescategorylist'))

def AddClothesSubCategories(request):
    form = ClothesSubCategoriesForm()
    if request.method == 'POST':
        form = ClothesSubCategoriesForm(request.POST,request.FILES)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/Clothes/addsubcategory.html', {'error': form.errors})
    return render(request, 'dashboard/Clothes/addsubcategory.html',{'form':form})

def ClothesSubCategorieslist(request):
    Subcategory = ClothesSubCategories.objects.all()
    return render(request,'dashboard/Clothes/subcategorylist.html',{'Subcategory':Subcategory})

class ClothesSubCategoriesUpdateView(UpdateView):
    template_name = 'dashboard/Clothes/editsubcategory.html'
    model = ClothesSubCategories
    fields = ['name']
    success_url ="/ClothesSubCategorieslist/"

def deleteClothesSubCategories(request,id):
    ClothesSubCategorieslist = ClothesSubCategories.objects.get(id=id)
    ClothesSubCategorieslist.delete()
    return HttpResponseRedirect(reverse('ClothesSubCategorieslist'))

def AddClothesBrand(request):
    form = ClothesBrandForm()
    if request.method == 'POST':
        form = ClothesBrandForm(request.POST,request.FILES)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/Clothes/addbrand.html', {'error': form.errors})
    return render(request, 'dashboard/Clothes/addbrand.html',{'form':form})

def ClothesBrandlist(request):
    Brand = ClothesBrand.objects.all()
    return render(request,'dashboard/Clothes/brandlist.html',{'Brand':Brand})

class ClothesBrandUpdateView(UpdateView):
    template_name = 'dashboard/Clothes/editbrand.html'
    model = ClothesBrand
    fields = ['name']
    success_url ="/brandlist/"

def deleteClothesBrand(request,id):
    brandlist = ClothesBrand.objects.get(id=id)
    brandlist.delete()
    return HttpResponseRedirect(reverse('brandlist'))

def AddClothes(request):
    form = ClothesForm()
    if request.method == 'POST':
        form = ClothesForm(request.POST,request.FILES)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/Clothes/addclothes.html', {'error': form.errors})
    return render(request, 'dashboard/Clothes/addclothes.html',{'form':form})

def Clotheslist(request):
    clothes = Clothes.objects.all()
    return render(request,'dashboard/Clothes/clotheslist.html',{'clothes':clothes})

class ClothesUpdateView(UpdateView):
    template_name = 'dashboard/Clothes/editclothes.html'
    model = Clothes
    fields = ['Name','MainCategory','SubCategory','Brand','Quantity','Color','Size','Price','Discount','finalprice','stock','Description','Image1','Image2','Image3','Image4']
    success_url ="/clotheslist/"

def deleteClothes(request,id):
    clotheslist = Clothes.objects.get(id=id)
    clotheslist.delete()
    return HttpResponseRedirect(reverse('clotheslist'))


#####################################################  MEDICINE  ########################################################

def AddMedicineCategory(request):
    form = MedicineCategoryForm()
    if request.method == 'POST':
        form = MedicineCategoryForm(request.POST,request.FILES)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/Medicine/addmedicinecategory.html', {'error': form.errors})
    return render(request, 'dashboard/Medicine/addmedicinecategory.html',{'form':form})

def MedicineCategorieslist(request):
    Category = MedicineCategory.objects.all()
    return render(request,'dashboard/Medicine/Medicinecategorylist.html',{'Category':Category})

class MedicineCategoriesUpdateView(UpdateView):
    template_name = 'dashboard/Medicine/editmedicinecategory.html'
    model = MedicineCategory
    fields = ['name']
    success_url ="/Medicinecategorylist/"

def deleteMedicineCategories(request,id):
    Medicinecategorylist = MedicineCategory.objects.get(id=id)
    Medicinecategorylist.delete()
    return HttpResponseRedirect(reverse('Medicinecategorylist'))


def AddMedicineBrand(request):
    form = MedicineBrandForm()
    if request.method == 'POST':
        form = MedicineBrandForm(request.POST,request.FILES)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/Medicine/addmedicinebrand.html', {'error': form.errors})
    return render(request, 'dashboard/Medicine/addmedicinebrand.html',{'form':form})

def MedicineBrandlist(request):
    Brand = MedicineBrand.objects.all()
    return render(request,'dashboard/Medicine/medicinebrandlist.html',{'Brand':Brand})

class MedicineBrandUpdateView(UpdateView):
    template_name = 'dashboard/Medicine/editmedicinebrand.html'
    model = MedicineBrand
    fields = ['name']
    success_url ="/medicinebrandlist/"

def deleteMedicineBrand(request,id):
    brandlist = MedicineBrand.objects.get(id=id)
    brandlist.delete()
    return HttpResponseRedirect(reverse('medicinebrandlist'))

def AddMedicine(request):
    form = MedicineForm()
    if request.method == 'POST':
        form = MedicineForm(request.POST,request.FILES)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/Medicine/addMedicine.html', {'error': form.errors})
    return render(request, 'dashboard/Medicine/addMedicine.html',{'form':form})

def Medicinelist(request):
    medicine = Medicine.objects.all()
    return render(request,'dashboard/Medicine/Medicinelist.html',{'medicine':medicine})

class MedicineUpdateView(UpdateView):
    template_name = 'dashboard/Medicine/editMedicine.html'
    model = Medicine
    fields = ['Name','Category','Brand','Description','Quantity','ManufactureDate','ExpireDate','Price','Discount','finalprice','Storage','Uses','Benefits','SideEffects','How_to_use','stock','Image1','Image2']
    success_url ="/Medicinelist/"

def deleteMedicine(request,id):
    Medicinelist = Medicine.objects.get(id=id)
    Medicinelist.delete()
    return HttpResponseRedirect(reverse('Medicinelist'))



######################################################  FAQ  #############################################################


def AddFAQ(request):
    form = FAQForm()
    if request.method == 'POST':
        form = FAQForm(request.POST)
       
        if form.is_valid():
            
            form.save()
        else:
            return render (request,'dashboard/FAQ/addFAQ.html', {'error': form.errors})
    return render(request, 'dashboard/FAQ/addFAQ.html',{'form':form})

def FAQlist(request):
    faq = FAQ.objects.all()
    return render(request,'dashboard/FAQ/FAQlist.html',{'faq':faq})

class FAQUpdateView(UpdateView):
    template_name = 'dashboard/FAQ/editFAQ.html'
    model = FAQ
    fields = ['question','answer']
    success_url ="/FAQlist/"

def deleteFAQ(request,id):
    FAQlist = FAQ.objects.get(id=id)
    FAQlist.delete()
    return HttpResponseRedirect(reverse('FAQlist'))