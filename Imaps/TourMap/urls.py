from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeHomeOdisha),
    path('KonarkSunTemple/', views.KonarkSunTemple),
    path('SimilipalNationalPark/', views.SimilipalNationalPark),
    path('UshaKothiWildlifeSanctuary/', views.UshaKothiWildlifeSanctuary),
    path('JagannathPuri/', views.JagannathPuri),
    path('ChilikaLake/', views.ChilikaLake),    
]
