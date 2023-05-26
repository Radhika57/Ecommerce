
from django.urls import path
from .views import *
from Useraccount import views
urlpatterns = [

path("signup/",RegisterView.as_view(),name="signup"),
path("admin/",LoginView.as_view(),name="login"),
path("logout/",views.logoutPage,name="logout"),
]