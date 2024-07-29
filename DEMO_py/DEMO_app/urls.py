from django.urls import path
from . import views
from .views import EmployeeListCreate
from .views import EmployeeRetrieveUpdateDestroy

# URLconfig
urlpatterns = [
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(), name='employee-detail'),
]