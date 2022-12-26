from os import environ

DEFAULT_RESOURCE = "/dashboard/home"
SHOW_ERROR_404 = False
ROOT_DIR = environ.get("DOCUMENT_ROOT", "/home/daniel/my_projects/mmt/rootsystem")
STATIC_DIR = "{}/static".format(ROOT_DIR)
DB_DIR = "core/database/data/"
