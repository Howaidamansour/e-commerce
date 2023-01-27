from django.urls import path
from . import views

app_name = 'auther'
urlpatterns = [
    path('', views.contactus, name='contact'),
    path('about', views.aboutus, name='about'),

]