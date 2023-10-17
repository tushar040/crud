"""
URL configuration for curd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import dynamic
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view1, name='home'),

    path('show', views.showData, name='showData'),
    path('add', views.addData, name='add'),
    path('create', views.createData, name='crt'),

    path('delete/<str:id>/', views.deleterecord, name='deleteid'),

    path('showByid/<str:id>/', views.showByid, name='showByid'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('showcat', views.showcat, name='Category_Name'),
    path('addcat', views.addcat, name='addcat'),
    path('showproduct', views.showproduct, name='Product_Name'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('deletepro/<str:id>/', views.deleteproduct, name='Product_Name'),
    path('deletecat/<str:id>/', views.deletecategory, name='Category_Name'),

    path('updatecat/<str:id>/', views.updatecat, name='catupdate'),

    path('update/<str:id>', views.update, name='update'),
    path('updaterecord/<str:id>', views.updaterecord, name='updaterecord'),

    path('temp', views.Details, name='temp'),
    path('addemp', views.addemp, name='addemp'),

    path('employees', views.employees, name="employees"),

    path('student', views.student, name="student"),
    path('addstud', views.addstud, name="addstud"),
    path('stud', views.stud, name="stud"),

    path('studentform', views.studentform, name="studentform"),
    path('insertData', views.insertData, name="insertData"),
    path('info', views.info, name="info"),


    path('form', views.form, name='form')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
