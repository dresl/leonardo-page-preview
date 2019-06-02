
try:
    from local_settings import APPS
except ImportError:
    pass

from django.apps import AppConfig

default_app_config = 'leonardo_page_preview.Config'

if 'leonardo_page_preview' in APPS:
    LEONARDO_APPS = ['leonardo_page_preview']

    LEONARDO_PAGE_EXTENSIONS = [
        'leonardo_page_preview.extension',
    ]


class Config(AppConfig):
    name = 'leonardo_page_preview'
    verbose_name = "leonardo-page-preview"
