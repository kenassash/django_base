from django.urls import path, include
from mainapp import views as mainapp

app_name = 'products'


urlpatterns = [
    path('', mainapp.products, name='products'),
    path('<int:pk>/', mainapp.products, name='products_category'),
    path('', mainapp.products_office, name='products_office'),
    path('', mainapp.products_classic, name='products_classic'),
]