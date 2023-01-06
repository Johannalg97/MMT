from cgi import FieldStorage
from string import Template

from config import STATIC_DIR
from core.tools.helpers import *
from modules.host import Host
from modules.sustrato import Sustrato
from modules.capa import Capa
# from core.functions.interpolacion import *
from settings import DB_DIR

class Matriz(object):
    """ Modelo """
    def __init__(self):
        self.matriz_id = 0
        self.angulo_i = ""
        self.angulo_f = ""
        self.logitudonda = ""
        self.pasos = ""
        self.polarizacion = ""
        self.sustrato = Sustrato() #objeto compositor
        self.host = Host() #objeto compositor
        self.capa_collection = [] #collecion de capas
        
    def insert(self):
        pass
    
    def update(self):
        pass
    
    def select(self):
        pass
    
    def delete(self):
        pass 
    

class MatrizView(object):
    """ Vista """
    
    @staticmethod
    def get_html(name):
        with open("{}/{}.html".format(STATIC_DIR, name),"r") as f:
            template = f.read()
        return template
        
    def calcular(self):
        base = MatrizView.get_html("base")
        inner = MatrizView.get_html("calcular")
        html = Template(base).safe_substitute(contenido=inner)
        
        show_html(html)
    

class MatrizController(object):
    """ Controlador """
    def __init__(self):
        self.model = Matriz()
        self.view = MatrizView()
        
    def calcular(self):
        self.view.calcular()
    
    def spectral(self):
        show_html("<br><h1>Pronto disponible...</h1>")
    
    def angular(self):
        form = FieldStorage()
        
#        self.model.theta = form['angulo'].value
#        self.model.wi = form['w_i'].value
#        # add materiales
#        try: 
#            for i in form['db']:
#                # get material 
#                path_to_db = "{}/{}.yml".format(DB_DIR, i.value)
#                data = get_schema_from_yaml(ruta=path_to_db)
#                self.model.materiales_collection.append(get_nk(data))
#        except TypeError:
#            path_to_db = "{}/{}.yml".format(DB_DIR, form['db'].value)
#            data = get_schema_from_yaml(ruta=path_to_db)
#            self.model.materiales_collection.append(get_nk(data))

        
#        show_html(f"Objeto {vars(self.model)}")
        show_html(form)
        
    def respuesta(self):
        form = FieldStorage()
        recurso = form['respuesta'].value
        
        url = "http://webmmt.local/matriz/{}".format(recurso)
        redirect(url)
        
