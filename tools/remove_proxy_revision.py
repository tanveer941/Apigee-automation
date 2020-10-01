from apigee_proxy import Proxies

def remove_proxy_revision_from_apigee(proxy_name, revision_number):
    proxy_obj = Proxies()
    # The download folder is mentioned in api_config.json
    proxy_obj.delete_revision_from_proxy(proxy_name, revision_number)

if __name__ == '__main__':
    proxy_name = 'Test-Proxy'
    revision_number = 6
    remove_proxy_revision_from_apigee(proxy_name, revision_number)