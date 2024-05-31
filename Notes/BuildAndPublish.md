# Build and Publish to the Cloud

1. **Remote Build (recommended build by default)**:
    - `func azure functionapp publish YOURFUNCTIONAPPNAME` 
    - Core Tools (command line) and Visual Studio Azure Functions extension use this by default
    - Dependencies obtained remotely based on contents of **requirements.txt** file
    - If using Linux, two additional app settings maybe created automatically in Azure:
        - ENABLE_ORYX_BUILD=true
        - SCM_DO_BUILD_DURING_DEPLOYMENT=true

2. **Local Build**
    - `func azure functionapp publish YOURFUNCTIONAPPNAME --build local`
    - Dependencies are obtained locally based on **requirements.txt** file
    - Packages are downloaded and installed locally and then published to the cloud. Larger deployment package.

3. **Custom Dependency Build**
    - Dependencies not found publicly via PyPI (Python Package Index)
    - Use extra index URL if packages are available from a custom package index
    - If packages aren't publicly available, put them in `__app__.python.packages` and install them locally first. Use --no-build option


4. **Azure Pipelines**:
    - Automated pipeline. Useful for PROD workloads
