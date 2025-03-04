from django.urls import path
from . import views

urlpatterns = [
    # ... your existing URL patterns ...
    path('listedcar-sub/', views.listedcar_sub, name='listedcar_sub'),
    path('certified-cars/', views.certified_cars_view, name='certified_cars'),
    path('certified-car/<int:car_id>/', views.certified_car_detail, name='certified_car_detail'),
    path('approved-certified-cars/', views.approved_certified_cars, name='approved_certified_cars'),
    # ... existing code ...
] 