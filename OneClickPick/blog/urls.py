from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name='bloghome'),
    # show the content present inside the blog in the blog post
    path('blogpost/<int:id>',views.blogpost,name='blogPost'),

]
'''whatever we are doing with the shop, the same thing we are doing with the blog'''
