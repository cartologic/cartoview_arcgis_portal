__author__ = 'kamal'
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

info = {
    "title": "ArcGIS Portal",
    "description": "Portal for ArcGIS Implementation.",
    "author": 'Cartologic',
    "home_page": 'http://cartologic.com/cartoview/apps/cartoserver',
    "help_url": "http://cartologic.com/cartoview/apps/cartoserver/help/",
    "tags": ['Feature Server'],
    "licence": 'BSD',
    "author_website": "http://www.cartologic.com",
    "single_instance": True
}


def install():
    import os, sys
    current_folder = os.path.dirname(__file__)
    sys.path.append(os.path.join(current_folder, 'libs'))
    from django.conf import settings
    settings.INSTALLED_APPS += ('cartoview.apps.cartoview_arcgis_portal.arcporal',)
    from django.db.models.loading import load_app
    load_app('cartoview.apps.cartoview_arcgis_portal.arcporal')


def uninstall():
    ContentType.objects.filter(app_label="arcporal").delete()
    ContentType.objects.filter(app_label="cartoview_arcgis_portal").delete()
