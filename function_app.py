import azure.functions as func
import logging
import pyodbc
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Retrieve the 'name' parameter from the request
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    # Database connection parameters
    server = os.environ.get('DB_SERVER', 'localhost')
    database = os.environ.get('DB_DATABASE', 'pro_1')
    username = os.environ.get('DB_USERNAME', 'root')
    password = os.environ.get('DB_PASSWORD', 'cogniwide@2024')
    driver = os.environ.get('DB_DRIVER', 'MySQL ODBC 8.0 ANSI Driver')

    # Attempt to connect to the database
    try:
        cnxn = pyodbc.connect(
            f'DRIVER={driver};SERVER={server};PORT={3306};DATABASE={database};UID={username};PWD={password};'
        )
        cursor = cnxn.cursor()
        

        # Perform database operations here
        # Example: Fetch all employees
        cursor.execute("SELECT fullname FROM Employee")
        rows = cursor.fetchall()

        employee_names = [row.fullname for row in rows]
        response_message = f"Employees: {', '.join(employee_names)}"

        cursor.close()
        cnxn.close()

    except pyodbc.Error as e:
        logging.error("Database connection failed:", e)
        return func.HttpResponse(
            "Database connection failed. Please check the logs for more details.",
            status_code=500
        )

    # Return response based on the request
    if name:
        return func.HttpResponse(f"Hello, {name}. {response_message}")
    else:
        return func.HttpResponse(
             f"This HTTP triggered function executed successfully. {response_message}",
             status_code=200
        )
