from cgi import FieldStorage

from config import STATIC_DIR
from core.tools.helpers import *
from core.functions.interpolacion import *
from settings import DB_DIR

class Matriz(object):
    """ Modelo """
    pass
    

class MatrizView(object):
    """ Vista """
    def calcular(self):
       with open("{}/calcular.html".format(STATIC_DIR),"r") as f:
            html = f.read()
       
       show_html(html)
    

class MatrizController(object):
    """ Controlador """
    def __init__(self):
        self.model = Matriz()
        self.view = MatrizView()
        
    def calcular(self):
        self.view.calcular()
    
    def procesar(self):
        form = FieldStorage()
        theta = form['angulo'].value
        w_i = form['w_i'].value
        db = form['db'].value
        # get material 
        path_to_db = "{}/{}.yml".format(DB_DIR, db)
        d_1 = get_schema_from_yaml(ruta=path_to_db)
        c_1 = get_nk(d_1)
        # Interpolacion
        
        
        show_html("data ")
