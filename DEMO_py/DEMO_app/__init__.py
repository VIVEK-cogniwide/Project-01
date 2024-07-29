import json
import os
import logging

import azure.functions as func

data = {
    [
    {
        "id": 1,
        "fullname": "Nagarjun Narayanasami",
        "age": "24",
        "designation": "HR Consultant",
        "salary": "1,00,000"
    },
    {
        "id": 2,
        "fullname": "Naren N",
        "age": "28",
        "designation": "Senior Software Engineer",
        "salary": "80,000"
    }
]
}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('python HTTP trigger function processed a request')
    return func.HttpResponse(json.dumps(data, indent=2),
            mimetype='application/json',
            status_code=200)
    