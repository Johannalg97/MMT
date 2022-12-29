from config import STATIC_DIR
from core.tools.helpers import *
# from core.functions.interpolacion import *
from settings import DB_DIR, ARG


class Materiales(object):
    pass
    
    
class MaterialesView(object):
    
    @staticmethod
    def get_html(name):
        with open("{}/{}.html".format(STATIC_DIR, name),"r") as f:
            template = f.read()
        return template
        
    def listar(self, cant):
        html = MaterialesView.get_html("materiales")
        string = []
        
        limite = cant + 1
        for i in range(1, limite):
            string.append(html)
            
        render = str("\n".join(string))
        show_ajax(render)
    
class MaterialesController(object):
    
    def __init__(self):
        self.model = Materiales()
        self.view = MaterialesView()
    
    def listar(self):
        cantidad = int(ARG)
        
        self.view.listar(cantidad)
        
        
