# AzureFunctionsPythonV2
Learn Azure Functions Python V2

# Why use Azure Functions and what problem does it solve?
Allows you to run your Python scripts/functions in Azure without having to create the infrastructure first


# Python developer article: https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=windows%2Cpowershell%2Cazure-cli&pivots=python-mode-decorators

# Steps to create Azure Functions

## Prerequisites:
-Install Func core tools: https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python

-Command line reference: https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference?tabs=v2

1. Open a terminal in Visual Studio Code (or whatever IDE you're using):
    func init NewFolderName --python -m v2

2. cd into NewFolderName and activate the Python virtual env (using PowerShell):
    ./.venv/scripts/activate

3. Install the requirements.txt file on the virtual env:
    python -m pip install -r requirements.txt
    OR
    pip install -r requirements.txt

5. Optional:
    Add any secrets/connection strings to the local.settings.json file as a new key value pair:
    "MyNewConnectionString": "Frank12345"
    Then in function_app.py or whichever file the function is in:
        import os
        connection_string = os.environ['MyNewConnectionString']


