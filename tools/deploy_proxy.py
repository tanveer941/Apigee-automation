from apigee_proxy import Proxies

def deploy_proxy_to_apigee(proxy_name, revision_number, environment):
    proxy_obj = Proxies()
    # Get the revision which is deployed for that environment
    # undeploy it, and then deploy the revision mentioned below
    proxy_obj.deploy_proxy_revision_in_environment(proxy_name, revision_number, environment)

if __name__ == '__main__':
    proxy_name = 'Test-Proxy'
    revision_number = 6
    environment = 'stage'
    deploy_proxy_to_apigee(proxy_name, revision_number, environment)