from django.urls import path
from aluguel_carros import views

urlpatterns = [
    path('', views.main_page, name='Pagina principal'),
]