import requests
import xmltodict
import pandas as pd

class CatastroAPI:
    def __init__(self):
        self.endpoint = "http://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCallejero.asmx/"
        self.request_timeout = 30
    
    def get(self, path, **kwargs):
        return getattr(self, f"_CatastroAPI__get_{path}")(**kwargs)

    def __get_provincias(self):
        response = requests.get(self.endpoint + "ConsultaProvincia", timeout=self.request_timeout)
        payload = xmltodict.parse(response.content, xml_attribs=False)
        
        provincias_df = pd.DataFrame(payload["consulta_provinciero"]["provinciero"]["prov"])
        provincias_df[["id", "name"]] = provincias_df[["cpine", "np"]]
        return provincias_df

    def __get_municipios(self, provincia):
        params = {
            "Provincia" : provincia,
            "Municipio" : ""
        }
        response = requests.get(self.endpoint + "ConsultaMunicipio", params=params, timeout=self.request_timeout)
        payload = xmltodict.parse(response.content, xml_attribs=False)

        municipios_df = pd.DataFrame(payload["consulta_municipiero"]["municipiero"]["muni"])
        municipios_df[["provincia_id", "id"]] = municipios_df["loine"].apply(pd.Series)
        municipios_df["name"] = municipios_df["nm"]
        return municipios_df[["provincia_id", "id", "name"]]

    def __get_vias(self, municipio):
        return None

    def __get_numeros(self, via):
        return None
