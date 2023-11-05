import requests
import xmltodict
import pandas as pd

class CatastroAPI:
    def __init__(self):
        self.endpoint = "http://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC"
        self.request_timeout = 30
    
    def get(self, path, **kwargs):
        return getattr(self, f"_CatastroAPI__get_{path}")(**kwargs)

    def __get_provincias(self):
        response = requests.get(self.endpoint + "/OVCCallejero.asmx/ConsultaProvincia", timeout=self.request_timeout)
        payload = xmltodict.parse(response.content, xml_attribs=False)
        
        provincias_df = pd.DataFrame(payload["consulta_provinciero"]["provinciero"]["prov"])
        provincias_df.columns = ["id", "name"]
        return provincias_df

    def __get_municipios(self, provincia):
        return None

    def __get_vias(self, municipio):
        return None

    def __get_numeros(self, via):
        return None
