# from django.shortcuts import render
# # Create your views here.
# # request -> response
# # your_app_name/views.py
# from rest_framework import generics
# from .models import Employee
# from .serializer import EmployeeSerializer
import logging
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Employee
from .serializer import EmployeeSerializer
logger = logging.getLogger(__name__)

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def delete(self, request, *args, **kwargs):
        logger.info(f"Delete method called with kwargs: {kwargs}")
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            response_data = {"message": f"Employee with ID {kwargs['pk']} deleted successfully."}
            logger.info(f"Sending response: {response_data}")
            return Response(response_data, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            logger.warning(f"Employee with ID {kwargs['pk']} not found.")
            return Response({"detail": f"Employee with ID {kwargs['pk']} not found."}, status=status.HTTP_404_NOT_FOUND)

