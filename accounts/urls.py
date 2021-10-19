from django.urls import path
from . import views 

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.view_profile, name='view_profile'),
    
   
]
