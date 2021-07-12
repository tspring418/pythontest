import logging
import datetime
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.debug('DEBUG- Python HTTP trigger function processed a request.')
    logging.info('INFO - Python HTTP trigger function processed a request.')
    logging.warning('WARNING - Python HTTP trigger function processed a request.')
    logging.error('ERROR  - Python HTTP trigger function processed a request.')
    logging.critical('CRITICAL - Python HTTP trigger function processed a request.')

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
