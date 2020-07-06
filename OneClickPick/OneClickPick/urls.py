"""REFER ALL THE FILES BECAUSE NOTES ARE PRESENT IN ALL THE FILES AND EXLPAINED ACCORDINGLY TO THE CODE"""
"""OneClickPick URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''EXPLANATION'''
'''We have to redirect people to the shop urls.py and should tell the mac.urls.py file that we have created an
app called as shop and for that we have to add an include statement.'''
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include('shop.urls')),
    path('blog/',include('blog.urls')),
    path('',views.index),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
'''initially the django framework will come through the OneClickPick URLs.py file and then it sees the
command in the urlpatterns and understands that someone has requested the OneClickPick urls.py file to take
them to the /shop and for that we have added the command called as incldue as the second argument to redirect
them to the shop urls.py page.'''
