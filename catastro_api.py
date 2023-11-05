class CatastroAPI:
    def __init__(self):
        self.endpoint = "http://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC"
        self.request_timeout = 30
    
    def get(self, path, **kwargs):
        return getattr(self, f"_CatastroAPI__get_{path}")(**kwargs)

    def __get_provincias(self):
        return None

    def __get_municipios(self, provincia):
        return None

    def __get_vias(self, municipio):
        return None

    def __get_numeros(self, via):
        return None
