import logging
import azure.functions as func

bp = func.Blueprint()

@bp.function_name('AdditionalHTTPFunction')
@bp.route(route="brandnewroute")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
        "Wow hello this worked!!!",
        status_code=200
        )