from django.urls import path
from first_app import views

urlpatterns = [
   path('',views.index,name='index'),
   path('index/',views.index,name='index'),
   path('newTemp/',views.newTemp,name='newTemp'),
     path('showForm/',views.showForm,name='showForm')
]