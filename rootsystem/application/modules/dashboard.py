# home applicacion
from string import Template

from config import STATIC_DIR
from core.tools.helpers import show_html

class DashboardController(object):
    
    @staticmethod
    def get_html(name):
        with open("{}/{}.html".format(STATIC_DIR, name),"r") as f:
            template = f.read()
        return template

    def home(self):
        base = DashboardController.get_html("base")
        inner = DashboardController.get_html("home")
        html = Template(base).safe_substitute(contenido=inner)
        
        show_html(html)
        
    def fundation_docs(self):
        with open("{}/index.html".format(STATIC_DIR),"r") as f:
            html = f.read()
        show_html(html)
