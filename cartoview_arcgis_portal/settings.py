__author__ = 'kamal'

import os, sys, datetime
from geonode.cartoview_settings import *
APP_NAME = "cartoview_arcgis_portal"
current_folder = os.path.dirname(__file__)
#because of using execfile instead of import in the project settings file current_folder will refer to project folder
current_folder = os.path.abspath(os.path.join(current_folder, os.path.pardir, 'cartoview', 'apps', APP_NAME))
sys.path.append(os.path.join(current_folder, 'libs'))
CARTOVIEW_APPS += ('cartoview.apps.%s.arcportal' % APP_NAME,)
