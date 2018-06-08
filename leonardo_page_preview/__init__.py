
from django.apps import AppConfig

default_app_config = 'leonardo_page_preview.Config'


LEONARDO_APPS = ['leonardo_page_preview']

LEONARDO_PAGE_EXTENSIONS = [
    'leonardo_page_preview.extension',
]


class Config(AppConfig):
    name = 'leonardo_page_preview'
    verbose_name = "leonardo-page-preview"
