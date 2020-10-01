from apigee_proxy import Proxies
from utils import zip_folder

def import_proxy_to_apigee(proxy_name, absolute_zip_file_pth):
    proxy_obj = Proxies()
    # The download folder is mentioned in api_config.json
    proxy_obj.import_proxy_into_apigee(proxy_name, absolute_zip_file_pth)

if __name__ == '__main__':
    # Mention the absolute location of the folder to be uploaded, if the proxy name already exists then it will
    # update the revision by a number higher else it will create a new proxy
    proxy_name = 'Test-Proxy'
    folder_to_zip = r'C:\Location\to\Proxy_folder'
    zip_folder(folder_to_zip)
    absolute_zip_file_pth = '{}.zip'.format(folder_to_zip)
    import_proxy_to_apigee(proxy_name, absolute_zip_file_pth)