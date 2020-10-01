import base64
from rest_apigee import RestClient
import json
import os

class Proxies(object):

    def __init__(self):
        # Prefill all the details to create proxy object
        with open('../api_config.json') as f:
            self.config_data = json.load(f)

        self.org_name = self.config_data['Orgname']
        self.username = self.config_data['Email']
        self.password = self.config_data['Password']

        userPass = self.username + ':' + self.password
        userPass = userPass.encode("utf-8")
        base64string = base64.b64encode(userPass).decode("utf-8")
        self.authentication = base64string

        self.proxy_server = self.config_data['ApigeeProxyServer']
        self.client = RestClient(token=self.authentication)

    def get_proxies_list(self):
        return self.client.get(url=self.proxy_server + self.config_data['GetProxies'].format(self.org_name))

    def export_proxy_to_local(self, proxy_name, revision_number):
        data_params = (
            ('format', 'bundle'),
        )
        export_url = self.proxy_server + self.config_data['ExportProxyRevision']\
            .format(self.org_name, proxy_name, revision_number)
        byte_data = self.client.get(url=export_url, params=data_params, response_object=True)
        file_name = os.path.join(self.config_data['DownloadFolder'], "{0}_{1}.zip".format(proxy_name, revision_number))
        with open(file_name, 'wb') as w:
            w.write(byte_data.content)
        print('File downloaded at : ' + file_name)
        return file_name

    def import_proxy_into_apigee(self, proxy_name, absolute_zip_file_pth):
        print("absolute_zip_file_pth::", absolute_zip_file_pth, proxy_name)
        byte_data = open(absolute_zip_file_pth, 'rb').read()
        files = {
            'file': ('My_proxy.zip', byte_data, 'application/x-gzip'),
        }
        import_url = self.proxy_server + self.config_data['ImportProxy']\
            .format(self.org_name, proxy_name)
        resp = self.client.file_post(url=import_url, files=files)
        print("Revision imported into Apigee\n", resp)

    def delete_revision_from_proxy(self, proxy_name, revision_number):

        delete_url = self.proxy_server + self.config_data['ExportProxyRevision']\
            .format(self.org_name, proxy_name, str(revision_number))
        resp = self.client.delete(url=delete_url)
        print("Delete response of proxy revision\n", resp)

    def deploy_proxy_revision_in_environment(self, proxy_name, revision_number, environment):
        deploy_url = self.proxy_server + self.config_data['DeployProxyRevision'] \
            .format(self.org_name, environment, proxy_name, str(revision_number))
        resp = self.client.post(url=deploy_url)
        print("Deployed {0} proxy of revision : {1} in {2} environment\n".
              format(proxy_name, revision_number, environment), resp)

    def undeploy_proxy_revision_in_environment(self, proxy_name, revision_number, environment):
        deploy_url = self.proxy_server + self.config_data['DeployProxyRevision'] \
            .format(self.org_name, environment, proxy_name, str(revision_number))
        resp = self.client.delete(url=deploy_url)
        print("UnDeployed {0} proxy of revision : {1} in {2} environment\n".
              format(proxy_name, revision_number, environment), resp)



