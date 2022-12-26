#!/usr/bin/env python3.10

from os.path import isfile

from settings import MODULE_PATH, PACKAGE, CONTROLLER, RESOURCE, HTTP_404,\
    HTTP_HTML, SHOW_ERROR_404, HTTP_REDIRECT, MODULE
from core.tools.helpers import redirect

error_module = error_resource = True

if isfile(MODULE_PATH):
    modulo = __import__(PACKAGE, fromlist=[CONTROLLER])
    controller = getattr(modulo, CONTROLLER)()
    error_module = False

if not error_module and hasattr(controller, RESOURCE):
    getattr(controller, RESOURCE)()
    error_resource = False

if error_module or error_resource:
    # error_header = "{}{}\n".format(HTTP_404, HTTP_HTML)
    # print(error_header if SHOW_ERROR_404 else HTTP_REDIRECT)
    redirect("http://webmmt.local/dashboard/home")
    
