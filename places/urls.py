from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('places/<int:place_id>/', views.place_detail, name='detail'),
]
