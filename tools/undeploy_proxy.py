from apigee_proxy import Proxies

def undeploy_proxy_from_apigee(proxy_name, revision_number, environment):
    proxy_obj = Proxies()
    proxy_obj.undeploy_proxy_revision_in_environment(proxy_name, revision_number, environment)

if __name__ == '__main__':
    proxy_name = 'Test-Proxy'
    revision_number = 5
    environment = 'stage'
    undeploy_proxy_from_apigee(proxy_name, revision_number, environment)