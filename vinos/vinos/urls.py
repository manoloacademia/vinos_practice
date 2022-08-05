from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('lista-vinos/', views.wine_list, name="wine_list"),
    path('crear-vinos/', views.create_wine, name="create_wine"),
    path('tipos/', views.brand_detail, name="brand_detail"),
    path('bodegas/', views.winery, name="winery"),
    path('search/', views.search_products, name="search")
]
