from django.db import models
from django.utils.translation import ugettext_lazy as _

from feincms import extensions


class Extension(extensions.Extension):

    def handle_model(self):

        # Add custom fields to the (Page) class
        self.model.add_to_class(
            'page_thumb',
            models.ImageField(
                verbose_name=_('Page thumbnail'),
                help_text=("Allows set thumbnail to this page."),
                blank=True, null=True,
                upload_to="page_thumbs/"
            ))

    def handle_modeladmin(self, modeladmin):
        # Add custom fields to the admin class
        modeladmin.add_extension_options(_('Thumbnail'), {
            'fields': ['page_thumb', ],
        })
