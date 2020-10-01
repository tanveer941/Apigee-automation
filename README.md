# Apigee utility tool
This tool facilitates the exporting of proxy configurations to local system, developing, 
modifying and then deploying back to the respective environments.
Adding new proxy and target endpoints can become cumbersome in the Apigee Edge console
Using the below export and import APIs will help for quicker development and deployment 
It will also help for segregating different target endpoints for Dev, Test and Stage environments

# Prefill data
To use this utility certain data needs to be prefilled in the `api_config.json`
- Credentials like username and password for the API authentication in JSON fields `Email` and `Password` respectively
- Apigee server name in `ApigeeProxyServer`
- Organisation name in `Orgname`

# Exporting proxy
- Execute the file `tools\export_proxy_to_local.py` with necessary parameters
- Enter the `proxy_name` and `revision_number`
- The `DownloadFolder` in `api_config.json` is the place where the proxy configurations are zipped, saved and extracted
- Local changes can be done to the XML files for the proxy and target endpoints

# Importing proxy zip configuration to Apigee server
- The XML files are added/removed/modified for policies/proxies/target endpoints
- Execute the file `tools\import_proxy_to_apigee.py` with necessary parameters
- Provide the `proxy_name` and `folder_to_zip` containing the XML files
- It will zip the contents and upload it to the Apigee server
- This will also validate if the bundle is correct or will fail if the configurations are incorrect
- If the proxy name is an existing one, it will upload the latest changes in a new revision number
- If the proxy does not exist, it will create a new proxy with that name

# Deploying a proxy revision
- Inorder to make available the recent changes to users, deployment is a must
- Execute the file `tools\deploy_proxy.py` with necessary parameters
- Provide the `proxy_name`, `environment` and `revision_number` of proxy
- This step can easily be done in the Apigee console
- If there is already a revision which is currently deployed then it needs to be undeployed first
- Then deploy the revision that you intend to

# Undeploying a proxy revision
- This step is usually done if another revision needs to be deployed
- Execute the file `tools\undeploy_proxy.py` with necessary parameters
- Provide the `proxy_name`, `environment` and `revision_number` of proxy
- This step can easily be done in the Apigee console

# Removing a proxy revision
- This is helpful to remove revisions that you do not need and to prevent accumulating them
- Execute the file `tools\remove_proxy_revision.py` with necessary parameters
- Provide the `proxy_name` and `revision_number` of proxy
- However revision numbers are important to track changes so this API should be rarely used