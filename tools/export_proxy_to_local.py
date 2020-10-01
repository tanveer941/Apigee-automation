from apigee_proxy import Proxies
from utils import extract_zipfile

def export_proxy_to_disk(proxy_name, revision_number):
    proxy_obj = Proxies()
    # The download folder is mentioned in api_config.json
    absolute_file_loc = proxy_obj.export_proxy_to_local(proxy_name, revision_number)
    # Extract the zip file
    extract_zipfile(absolute_file_loc)
    print(f'{absolute_file_loc} file extracted!!')
    print(f'Working folder to modify the proxy details like its endpoints are in the XML files')

if __name__ == '__main__':
    proxy_name = 'Test-Proxy'
    revision_number = 4
    # The download folder is mentioned in api_config.json
    export_proxy_to_disk(proxy_name, revision_number)