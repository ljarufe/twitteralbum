from __future__ import unicode_literals

import os
import urllib

from django.db import models
from django.core.files import File


class Album(models.Model):
    # TODO: user could be a foreign key
    # TODO: use translations
    user = models.CharField(u'user', max_length='100')
    image = models.ImageField(
        u'image', upload_to='albums', blank=True, unique=True)

    def __unicode__(self):
        return self.user

    # TODO: create a class method
    def save(self, *args, **kwargs):
        super(Album, self).super(*args, **kwargs)
        self.image_url = kwargs.pop('image_url', None)
        if self.image_url:
            result = urllib.urlretrieve(self.image_url)
            self.image.save(
                os.path.basename(self.image_url), File(open(result[0])))
