# Resources Needed Before Deploying Functions to Azure

1. **Function App**
    - Different plan options (hosted on an App Service Plan):
    - Main doc: <https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale>
        - **Consumption**:
            - Only charged when Function App runs
            - Free grants (execution time/total executions)
        - **Premium**:
            - Different premium plans available
            - Pre-warmed workers, more powerful instances, network  security, etc.
        - **Dedicated (App Service)**:
            - Deploying Function App in an existing App Service Plan
            - Not consumption-based costs. Billed for the plan

2. **Storage Account**:
    - General-purpose that supports Blobs, Queues, Table Storage. Not blob-only storage, etc.
    - Blob: Used by default to store Function App keys (function/host/system keys)
    - Files: Stores/runs Function App code in Consumption and Premium Plan
    - Queue: Used by default for task hubs (durable functions), failure/retry handling in specific triggers
    - Table: Used by default for task hubs (durable functions)

3. **Application Insights (optional)**:
    - Provides additional insights/logging for Azure Functions
