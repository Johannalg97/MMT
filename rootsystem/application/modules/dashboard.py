from cgi import FieldStorage
from string import Template
from os import environ

from config import STATIC_DIR
from core.tools.helpers import show_html

class DashboardController(object):

    def home(self):
        show_html("hola Mundo MMT")
