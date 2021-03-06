"""HomeSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from Contact import views
from django.conf.urls.static import static

admin.sites.AdminSite.site_header = 'StackOverflow Clone Administration'
admin.sites.AdminSite.site_title = 'StackOverflow Clone Administration'
admin.sites.AdminSite.index_title = 'Ankit Administration'

urlpatterns = [
    url(r'^secretadmin/', admin.site.urls),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name='search'),
    path('profile/',views.profile,name='profile'),
    path('users/',views.users,name='users'),

    #app urls
     path('blog/', include('blog.urls')),
     path('account/', include('Authentication.urls')),
     path('home/', include('StackoverflowClone.urls')),
    
]

handler404 = 'Contact.views.error_404_view' 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





