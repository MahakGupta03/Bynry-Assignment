from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('submit/', views.submit_request, name='submit_request'),
    path('support/', views.support_dashboard, name='support_dashboard'),
    path('support/update/<int:pk>/', views.update_request, name='update_request'),
]