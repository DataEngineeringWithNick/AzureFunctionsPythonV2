import azure.functions as func
import logging

bp = func.Blueprint()

#HTTP Trigger
@bp.function_name('test_api33333')
@bp.route(route="myroute", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
        "Wow hello this worked!!!",
        status_code=200
        )