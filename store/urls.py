from django.urls import path
from . import views
urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:catagory_slug>/',
         views.store, name='product_by_catagory'),
    path('category/<slug:catagory_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
    path('search/', views.search, name="search")
]
