""" over here actually urls.py file is not existing. we have created it and then we have to tell the urls.py file of
 the  project (OneClickPick)that we have included a urls.py file in the shop app. so the changes are done accordingly
 in the OneClickPick urls.py file using the include command.
 just copied the code present in the OneClickPick urls.py file and pasted over here. the first two lines.
 from django.contrib import admin
no need of the admin over here as there is no use of database currently"""
from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name='ShopHome'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('tracker/',views.tracker,name='trackingstatus'),
    path("search/",views.search,name="Search"),
    path("products/<int:myid>",views.productview,name='productview'),
    path('checkout/',views.checkout,name='checkout'),
    path('handlerequest/',views.handlerequest,name='HandleRequest'),
]
''' after the user is being directed from the OneClickPick URLs.py page to this page, then the framework will go
through the commands present in theh urlpatterns and over there we have included the second argument as views.index
which is nothing but we are commanding it to move on to the views.py page and execute the function index over there
The first argument in the ath command is an empty string which implies that we dont require to append anything in the
url after /shop'''
