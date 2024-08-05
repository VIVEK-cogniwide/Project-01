import os
import logging
import azure.functions as func
from django.core.wsgi import get_wsgi_application
import json

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DEMO_py.settings')  # Ensure this path is correct

# Initialize Django
import django
django.setup()

# Import your Django models here
from DEMO_app.models import Employee  # Ensure this path is correct

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if req.method == "POST":
        try:
            req_body = req.get_json()
            fullname = req_body.get('fullname')
            age = req_body.get('age')
            designation = req_body.get('designation')
            salary = req_body.get('salary')

            if not all([fullname, age, designation, salary]):
                return func.HttpResponse(
                    json.dumps({"error": "Missing employee details in the request body."}),
                    status_code=400,
                    mimetype="application/json"
                )

            employee = Employee(
                fullname=fullname,
                age=age,
                designation=designation,
                salary=salary
            )
            employee.save()

            return func.HttpResponse(
                json.dumps({"message": f"Employee {fullname} created successfully."}),
                status_code=201,
                mimetype="application/json"
            )

        except ValueError:
            return func.HttpResponse(
                json.dumps({"error": "Invalid input. Please provide valid JSON."}),
                status_code=400,
                mimetype="application/json"
            )

    else:  # Handle GET requests
        name = req.params.get('name')
        if not name:
            try:
                req_body = req.get_json()
            except ValueError:
                pass
            else:
                name = req_body.get('name')

        if name:
            try:
                employee = Employee.objects.get(fullname=name)
                response_data = {
                    "fullname": employee.fullname,
                    "age": employee.age,
                    "designation": employee.designation,
                    "salary": employee.salary
                }
            except Employee.DoesNotExist:
                return func.HttpResponse(
                    json.dumps({"error": f"No employee found with the name {name}."}),
                    status_code=404,
                    mimetype="application/json"
                )

            return func.HttpResponse(
                json.dumps(response_data),
                status_code=200,
                mimetype="application/json"
            )
        else:
            return func.HttpResponse(
                json.dumps({"error": "No name provided."}),
                status_code=400,
                mimetype="application/json"
            )
