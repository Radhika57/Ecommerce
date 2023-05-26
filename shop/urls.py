from shop import shop_views
from django.urls import path

urlpatterns = [
    path("",shop_views.maincontent,name='home'),
    path("about/",shop_views.about,name='about'),
    path("faq/",shop_views.FAQ,name='faq'),
    path("contactus/",shop_views.contactus,name='contactus'),
    path("shop/",shop_views.shop,name='shop'),
    path("shop1/",shop_views.shop1,name='shop1'),
    path("shop2/",shop_views.shop2,name='shop2'),
    path("shop3/",shop_views.shop3,name='shop3'),
    path("meatdetails/<int:id>",shop_views.meatdetails,name='meatdetails'),
    path("fmcgdetails/<int:id>",shop_views.fmcgdetails,name='fmcgdetails'),
    path("clothesdetails/<int:id>",shop_views.clothesdetails,name='clothesdetails'),
    path("medicinedetails/<int:id>",shop_views.medicinedetails,name='medicinedetails'),
    path("terms&conditions",shop_views.termsconditions,name='terms&conditions'),
]
