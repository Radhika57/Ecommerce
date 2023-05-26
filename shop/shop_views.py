from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from dashboard.models import *
from shop.models import *

# Create your views here.
def maincontent(request):
    return render(request,'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def FAQ(request):
    return render(request,'shop/faq.html')

def contactus(request):
    return render(request,'shop/contact.html')

def shop(request):
    product = Meat.objects.all()
    category = MeatCategories.objects.all()
    return render(request,'shop/shop.html',{'product':product,'category':category})

def shop1(request):
    fmcg = FMCG.objects.all()
    category = FMCGCategories.objects.all()
    subcategory = FMCGSubCategories.objects.all()
    return render(request,'shop/shop1.html',{'fmcg':fmcg,'category':category,'subcategory':subcategory})

def shop2(request):
    medicine = Medicine.objects.all()
    brand = MedicineBrand.objects.all()
    category = MedicineCategory.objects.all()
    return render(request,'shop/shop2.html',{'medicine':medicine,'brand':brand,'category':category})

def shop3(request):
    clothes = Clothes.objects.all()
    brand = ClothesBrand.objects.all()
    category = ClothesCategories.objects.all()
    subcategory = ClothesSubCategories.objects.all()
    return render(request,'shop/shop3.html',{'clothes':clothes,'brand':brand,'category':category,'subcategory':subcategory})


def meatdetails(request,id):
    meat = Meat.objects.get(id=id)
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        try:
            rating_value = int(rating_value)
        except ValueError:
            rating_value = None

        review = request.POST.get('review')
        name = request.POST.get('name')

        if rating_value is not None:
            review = MeatReview(meat=meat, rating=rating_value, review=review,name=name)
            review.save()
    return render(request,'shop/meat_details.html',{"meat":meat})

def fmcgdetails(request,id):
    fmcg = FMCG.objects.get(id=id)
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        try:
            rating_value = int(rating_value)
        except ValueError:
            rating_value = None

        review = request.POST.get('review')
        name = request.POST.get('name')

        if rating_value is not None:
            review = FMCGReview(fmcg=fmcg, rating=rating_value, review=review,name=name)
            review.save()
    return render(request,'shop/fmcg_details.html',{"fmcg":fmcg})

def clothesdetails(request,id):
    clothes = Clothes.objects.get(id=id)
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        try:
            rating_value = int(rating_value)
        except ValueError:
            rating_value = None

        review = request.POST.get('review')
        name = request.POST.get('name')

        if rating_value is not None:
            review = ClothesReview(clothes=clothes, rating=rating_value, review=review,name=name)
            review.save()
    return render(request,'shop/clothes_details.html',{"clothes":clothes})

def medicinedetails(request,id):
    medicine = Medicine.objects.get(id=id)
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        try:
            rating_value = int(rating_value)
        except ValueError:
            rating_value = None

        review = request.POST.get('review')
        name = request.POST.get('name')

        if rating_value is not None:
            review = MedicineReview(medicine=medicine, rating=rating_value, review=review,name=name)
            review.save()
    return render(request,'shop/medicine_details.html',{"medicine":medicine})

def termsconditions(request):
    return render(request,'shop/terms&conditions.html')
