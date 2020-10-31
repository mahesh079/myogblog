from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="contactus"),
    path("tracker/",views.tracker,name="Trackingstatus"),
    path("search/",views.search,name="search"),
    path("products/<int:id>",views.productview,name="productview"),
    path("checkout/",views.checkout,name="Checkout")
]
