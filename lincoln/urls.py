from django.urls import path
from lincoln import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('departments/',views.departments,name='departments'),
    path('doctor/',views.doctor,name='doctor'),
    path('readmore/',views.readme1,name='readme1'),
    path('readmore/',views.readmore,name='readmore'),
    path('readmore/',views.readmore1,name='readmore1'),





]





