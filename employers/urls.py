from django.urls import path
from .views import EmployerListCreateView, EmployerDetailView

urlpatterns = [
    path('', EmployerListCreateView.as_view(), name='employer-list'),
    path('<int:pk>/', EmployerDetailView.as_view(), name='employer-detail'),
]
