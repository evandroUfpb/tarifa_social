import requests
from urllib3.exceptions import InsecureRequestWarning
import zipfile
import os


class DownloadandExtractData:
    def __init__(self):
        self.cwd = os.getcwd()
        self.url ="https://dadosabertos.aneel.gov.br/dataset/0ffe45bc-b0bc-4c18-99ab-e97e94841418/resource/e6cb4eb6-3ddb-4fc7-8780-29645f9b35cf/download/tarifasocial.csv"
        self.path = self.cwd +'/data/'
    # Suppress only the single warning from urllib3 needed.
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    # Download file
    def download_file(self):
        try:
            os.mkdir(self.cwd+'/data')
        except:
            pass
        local_filename = self.url.split('/')[-1]
        r = requests.get(self.url, stream=True, verify=False)
        with open(self.path + local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
            print("Download do arquivo "+local_filename+" concluido!")
        return local_filename

    def extract_file(self,file_name):
        stories_zip = zipfile.ZipFile(self.path + file_name)
        for file in stories_zip.namelist():
            info = stories_zip.getinfo(file)
            stories_zip.extract(file, self.path)
            print("Arquivo "+file+" extraído com sucesso!")
        stories_zip.close()

