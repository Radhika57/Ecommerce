from dashboard import dashboard_views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("dashboard/",dashboard_views.dashboard,name='dashboard'),
    
    #############################################  Meat URLs  #########################################################
    
    path("addmeatcategory/",dashboard_views.AddMeatCategories,name='addmeatcategory'),
    path("meatcategorylist/",dashboard_views.MeatCategorylist,name='meatcategorylist'),
    path("editmeatcategory/<int:pk>", dashboard_views.MeatCategoryUpdateView.as_view(), name="editmeatcategory"),
    path('deletemeatcategory/<int:id>',dashboard_views.deletemeatcategory,name="deletemeatcategory"),
    
    path("addmeat/",dashboard_views.AddMeat,name='addmeat'),
    path("meatlist/",dashboard_views.Meatlist,name='meatlist'),
    path("editmeat/<int:pk>", dashboard_views.MeatUpdateView.as_view(), name="editmeat"),
    path('deletemeat/<int:id>',dashboard_views.deletemeat,name="deletemeat"),
    
    ######################################  FMCG URLs  ###############################################################
    
    path("addfmcgcategory/",dashboard_views.AddFMCGCategory,name='addfmcgcategory'),
    path("fmcgcategorylist/",dashboard_views.FMCGCategorylist,name='fmcgcategorylist'),
    path("editfmcgcategory/<int:pk>", dashboard_views.FMCGCategoryUpdateView.as_view(), name="editfmcgcategory"),
    path('deletefmcgcategory/<int:id>',dashboard_views.deletefmcgcategory,name="deletefmcgcategory"),
    
    path("addfmcgsubcategory/",dashboard_views.AddFMCGSubCategory,name='addfmcgsubcategory'),
    path("fmcgsubcategorylist/",dashboard_views.FMCGSubCategoryList,name='fmcgsubcategorylist'),
    path("editfmcgsubcategory/<int:pk>", dashboard_views.FMCGSubCategoryUpdateView.as_view(), name="editfmcgsubcategory"),
    path('deletefmcgsubcategory/<int:id>',dashboard_views.deletefmcgsubcategory,name="deletefmcgsubcategory"),
    
    path("addfmcgbrand/",dashboard_views.AddFMCGbrand,name='addfmcgbrand'),
    path("fmcgbrandlist/",dashboard_views.FMCGBrandList,name='fmcgbrandlist'),
    path("editfmcgbrand/<int:pk>", dashboard_views.FMCGBrandUpdateView.as_view(), name="editfmcgbrand"),
    path('deletefmcgbrand/<int:id>',dashboard_views.deletefmcgBrand,name="deletefmcgbrand"),
    
    path("addfmcg/",dashboard_views.AddFMCG,name='addfmcg'),
    path("fmcglist/",dashboard_views.FMCGlist,name='fmcglist'),
    path("editfmcg/<int:pk>", dashboard_views.FMCGUpdateView.as_view(), name="editfmcg"),
    path('deletefmcg/<int:id>',dashboard_views.deletefmcg,name="deletefmcg"),
    
    
    #########################################  Clothes URLs  ###########################################################
    
    
    path("addcategory/",dashboard_views.AddClothesCategories,name='addcategory'),
    path("clothescategorylist/",dashboard_views.ClothesCategorieslist,name='clothescategorylist'),
    path("editclothescategory/<int:pk>", dashboard_views.ClothesCategoriesUpdateView.as_view(), name="editclothescategory"),
    path('deleteclothescategory/<int:id>',dashboard_views.deleteClothesCategories,name="deleteclothescategory"),
    
    path("addsubcategory/",dashboard_views.AddClothesSubCategories,name='addsubcategory'),
    path("ClothesSubCategorieslist/",dashboard_views.ClothesSubCategorieslist,name='ClothesSubCategorieslist'),
    path("editclothessubcategory/<int:pk>", dashboard_views.ClothesSubCategoriesUpdateView.as_view(), name="editclothessubcategory"),
    path('deleteclothessubcategory/<int:id>',dashboard_views.deleteClothesSubCategories,name="deleteclothessubcategory"),
    
    path("addbrand/",dashboard_views.AddClothesBrand,name='addbrand'),
    path("brandlist/",dashboard_views.ClothesBrandlist,name='brandlist'),
    path("editbrand/<int:pk>", dashboard_views.ClothesBrandUpdateView.as_view(), name="editbrand"),
    path('deletebrand/<int:id>',dashboard_views.deleteClothesBrand,name="deletebrand"),
    
    path("addclothes/",dashboard_views.AddClothes,name='addclothes'),
    path("clotheslist/",dashboard_views.Clotheslist,name='clotheslist'),
    path("editclothes/<int:pk>", dashboard_views.ClothesUpdateView.as_view(), name="editclothes"),
    path('deleteclothes/<int:id>',dashboard_views.deleteClothes,name="deleteclothes"),
    
    
    #########################################  Medicine URLs  ###########################################################
    
    
    path("addmedicinecategory/",dashboard_views.AddMedicineCategory,name='addmedicinecategory'),
    path("Medicinecategorylist/",dashboard_views.MedicineCategorieslist,name='Medicinecategorylist'),
    path("editmedicinecategory/<int:pk>", dashboard_views.MedicineCategoriesUpdateView.as_view(), name="editmedicinecategory"),
    path('deleteMedicineCategories/<int:id>',dashboard_views.deleteMedicineCategories,name="deleteMedicineCategories"),
   
    path("addmedicinebrand/",dashboard_views.AddMedicineBrand,name='addmedicinebrand'),
    path("medicinebrandlist/",dashboard_views.MedicineBrandlist,name='medicinebrandlist'),
    path("editmedicinebrand/<int:pk>", dashboard_views.MedicineBrandUpdateView.as_view(), name="editmedicinebrand"),
    path('deletemedicinebrand/<int:id>',dashboard_views.deleteMedicineBrand,name="deletemedicinebrand"),
    
    path("addMedicine/",dashboard_views.AddMedicine,name='addMedicine'),
    path("Medicinelist/",dashboard_views.Medicinelist,name='Medicinelist'),
    path("editMedicine/<int:pk>", dashboard_views.MedicineUpdateView.as_view(), name="editMedicine"),
    path('deletemedicine/<int:id>',dashboard_views.deleteMedicine,name="deletemedicine"),
    
    
    ###############################################  FAQ URLs  ##########################################################
    
    path("addFAQ/",dashboard_views.AddFAQ,name='addFAQ'),
    path("FAQlist/",dashboard_views.FAQlist,name='FAQlist'),
    path("editFAQ/<int:pk>", dashboard_views.FAQUpdateView.as_view(), name="editFAQ"),
    path('deleteFAQ/<int:id>',dashboard_views.deleteFAQ,name="deleteFAQ"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)