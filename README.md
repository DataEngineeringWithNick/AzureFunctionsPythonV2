# YouTube Videos:

- Part 1 (Local Setup and Examples): [YouTube Video Part 1](https://www.youtube.com/watch?v=I-kodc4bs4I)

- Part 2 (Deploy and Use in Azure): [YouTube Video Part 2](https://www.youtube.com/watch?v=_349bwtFkE8)

# Why Use Azure Functions and What Problem Does it Solve?
Allows you to run your Python scripts/functions in Azure without having to create the infrastructure first

**Python developer article**: 
[Python Functions V2 Developer Guide](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=windows%2Cpowershell%2Cazure-cli&pivots=python-mode-decorators)

# Steps to create Azure Functions Locally

## Local Setup Prerequisites and Initial Configuration:
- Install Func core tools: [Install Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python)

- Command line reference: [Command Line Reference](https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference?tabs=v2)

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