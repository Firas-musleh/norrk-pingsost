from . import views
from django.urls import path

app_name='ost'

urlpatterns = [
    path('',views.all_prodcut, name='product_list'),
    path('<slug:slug>', views.one_prodcut, name='one_prodcut'), 
    path('about_us/', views.about_us, name='about_us'),
   
   
]
