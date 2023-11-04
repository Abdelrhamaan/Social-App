from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_img, name='create' ),   
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'), 
    # path('like/', views.image_like, name='like'), 
    path('like/', views.image_like, name='like'),
    path('', views.image_list, name='list'),
    path('ranking/', views.image_ranking, name='ranking'),
]