from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="BlogHome"),
    path("blogpost/<int:id>",views.blogpost,name="blogpost"),
    path("search/",views.search,name="search"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path('contactus/',views.contactus,name="contactus"),
    path('signup/',views.signup,name="signup"),
    path('signup2/',views.signup2,name="signup2"),
    path('login/',views.login2,name="login2"),
    path('login2/',views.login3,name="login3"),
    path('logout/',views.logout2,name='logout2'),
    # api to post comment
    path('postComment',views.postComment,name="postComment")
]
