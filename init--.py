import azure.functions as func
from azure_functions_django import get_wsgi_application 

app = get_wsgi_application()

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.WsgiMiddleware(app).handle(req, context)
