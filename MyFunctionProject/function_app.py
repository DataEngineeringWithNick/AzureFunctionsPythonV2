import azure.functions as func
import datetime
import json
import logging
import csv
import codecs
from additional_functions import bp

app = func.FunctionApp()
app.register_blueprint(bp)


@app.function_name('test_my_api2')
@app.route(route="newend", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    name = req.params.get('name')
    message = f"Wow hello, {name}, this worked!!!!"
    
    return func.HttpResponse(
        message,
        status_code=200
        )


@app.function_name(name="BlobTrigger1")
@app.blob_trigger(arg_name="myblob", 
                  path="mynewcontainer/People.csv",
                  connection="AzureWebJobsStorage")
def test_function(myblob: func.InputStream):
   logging.info(f"Python blob trigger function processed blob WOW SO COOL!!! \n"
                f"Name: {myblob.name}"
                )


@app.function_name(name="BlobInputTrigger2")
@app.blob_trigger(arg_name="myblob2",
                  path="mynewcontainer/People.csv",
                  connection="AzureWebJobsStorage")
def main(myblob2: func.InputStream):
    logging.info("Attempting this function")
    reader=csv.reader(codecs.iterdecode(myblob2,'utf-8'))
    for line in reader:
        logging.info(line)
