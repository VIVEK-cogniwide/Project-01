import azure.functions as func
import logging
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')


    if name == 'azureuser':
        try:
            response = requests.get("http://127.0.0.1:8000/DEMO_app/employees/")
            response.raise_for_status() 
            api_data = response.text
            return func.HttpResponse(
                api_data,
                status_code=response.status_code,
                mimetype="application/json"
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching from API: {e}")
            # return func.HttpResponse(
            #     "Error fetching data from API",
            #     status_code=500
            # )
    
   
    return func.HttpResponse(
        f"Hello, {name}!",
        status_code=200
    )

@app.route(route="http_trigger", auth_level=func.AuthLevel.undefined)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.route(route="http_trigger", auth_level=func.AuthLevel.FUNCTION)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )