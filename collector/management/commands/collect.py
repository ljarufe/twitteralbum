from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from twython import Twython

from albums.models import Album


class Command(BaseCommand):
    help = 'Collect photos'

    def handle(self, *args, **options):
        # TODO: send to utils and store the access token
        twitter = Twython(
            settings.APP_KEY, settings.APP_SECRET, oauth_version=2)
        access_token = twitter.obtain_access_token()
        # TODO: let this stay here
        twitter = Twython(settings.APP_KEY, access_token=access_token)
        results = twitter.cursor(twitter.search, q='#carnival filter:images')
        for result in results:
            if 'media' in result['entities']:
                for media in result['entities']['media']:
                    # TODO: store the media in a variable and use it at the bottom
                    album = Album(user=result['user']['name'])
                    album.save(image_url=media['media_url'])
            elif 'retweeted_status' in result:
                if 'media' in result['retweeted_status']:
                    media_data = result['retweeted_status']['entities']['media']
                    for media in media_data:
                        album = Album(user=result['user']['name'])
                        album.save(image_url=media['media_url'])
