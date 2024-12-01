from django.urls import path
from . import views

urlpatterns = [
    path('dynamic-fields/', views.dynamic_fields, name='dynamic-fields'),
    path('employees/', views.employee_management, name='employee-management'),
]
