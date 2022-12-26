# home applicacion
from config import STATIC_DIR
from core.tools.helpers import show_html

class DashboardController(object):

    def home(self):
        with open("{}/home.html".format(STATIC_DIR),"r") as f:
            html = f.read()
        show_html(html)
