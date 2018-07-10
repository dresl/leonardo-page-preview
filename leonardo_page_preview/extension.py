from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.media.models import Image
from feincms import extensions

class Extension(extensions.Extension):

    def handle_model(self):

        # Add custom fields to the (Page) class
        self.model.add_to_class(
            'page_thumb',
            models.ForeignKey(
                Image,
                verbose_name=_('Page thumbnail'),
                help_text=("Allows set thumbnail to this page (Including video)."),
                blank=True, null=True,
            ))

    def handle_modeladmin(self, modeladmin):
        # Add custom fields to the admin class
        modeladmin.add_extension_options(_('Thumbnail'), {
            'fields': ['page_thumb', ],
        })
