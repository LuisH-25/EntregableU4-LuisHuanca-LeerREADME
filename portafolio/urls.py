from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('', views.PortafolioView.as_view(), name="index"),
    path('create/<int:id>', views.PortafolioCreate.as_view(), name="create"),
    path('delete/<int:id>', views.deletePortafolio, name="delete"),
    #path('verPortafolios/', views.PortafolioView.as_view(), name="verPortafolios"),
]
