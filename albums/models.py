from __future__ import unicode_literals

from datetime import datetime

from django.db import models


class Album(models.Model):
    user = models.CharField(u'user', max_length=100)
    image = models.ImageField(
        u'image', upload_to='albums')
    image_url = models.URLField(u'image URL', unique=True)
    twitter_creation_date = models.DateTimeField(u'twitter creation date')
    creation_date = models.DateTimeField(u'creation date', default=datetime.now)
    favorite_count = models.IntegerField(u'favorite count', default=0)

    def __unicode__(self):
        return self.image_url
