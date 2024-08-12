import azure.functions as func
import logging
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="employee")
def employee(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    
    base_url = "http://127.0.0.1:8000/DEMO_app/employees/"

    
    employee_id = req.params.get('id')
    method = req.method.lower()

    try:
        if method == 'get':
           
            url = f"{base_url}{employee_id}/" if employee_id else base_url
            response = requests.get(url)
            logging.info(f"GET request sent to {url}, response status: {response.status_code}")
            return func.HttpResponse(response.content, status_code=response.status_code, mimetype="application/json")

        elif method == 'post':
            
            employee_data = req.get_json()
            response = requests.post(base_url, json=employee_data)
            logging.info(f"POST request sent to {base_url}, response status: {response.status_code}")
            return func.HttpResponse(response.content, status_code=response.status_code, mimetype="application/json")

        elif method == 'delete' and employee_id:
           
            url = f"{base_url}{employee_id}/"
            response = requests.delete(url)
            logging.info(f"DELETE request sent to {url}, response status: {response.status_code}")
            return func.HttpResponse(response.content, status_code=response.status_code, mimetype="application/json")

        else:
            return func.HttpResponse("Method not allowed or missing ID for delete.", status_code=405)

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return func.HttpResponse("Failed to connect to Django API.", status_code=500)
