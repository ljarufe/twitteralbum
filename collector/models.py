from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from twython import Twython


class TwitterConnector(models.Model):
    token = models.CharField(u'token', max_length=250)

    def __unicode__(self):
        return self.token

    def save(self, *args, **kwargs):
        if TwitterConnector.objects.all().exists():
            TwitterConnector.objects.all().delete()
        twitter = Twython(
            settings.APP_KEY, settings.APP_SECRET, oauth_version=2)
        self.token = twitter.obtain_access_token()
        super(TwitterConnector, self).save(*args, **kwargs)

    def get_results(self, *args):
        self.twitter = Twython(settings.APP_KEY, access_token=self.token)

        return self.twitter.cursor(self.twitter.search, q=" ".join(args))