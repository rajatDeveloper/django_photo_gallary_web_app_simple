from django.urls import path
from . import views


urlpatterns = [
   path('',views.gallery,name='gallery'),
   path('add/',views.addPhoto,name='add'),
   path('photo/<str:pk>/',views.viewPhoto,name='photo'),
   path('delete_photo/<int:pk>',views.delete_photo,name="delete_photo"),
]