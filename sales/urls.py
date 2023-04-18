from django.urls import path
from . import views

app_name ='sales'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:seat_id>/', views.detail, name='detail'),
    path('seat/create/', views.seat_create, name='seat_create'),
    path('seat/modify/<int:seat_id>/', views.seat_modify, name='seat_modify'),
    path('seat/delete/<int:seat_id>/', views.seat_delete, name='seat_delete'),
]