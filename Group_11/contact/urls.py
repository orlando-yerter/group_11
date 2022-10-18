from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from contact import views
urlpatterns = [
   
   
    path('',views.contact, name="contact"),
    
    
]