from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand

from albums.forms import AlbumForm
from albums.models import Album
from collector.models import TwitterConnector


class Command(BaseCommand):
    help = 'Collect photos'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.albums = Album.objects.all()
        self.counter = self.albums.count()

    def _save(self, **kwargs):
        album_form = AlbumForm(data=kwargs)
        if album_form.is_valid():
            album_form.save()
            self.counter += 1
            if self.counter % 100 and self.counter <= 500:
                email = EmailMessage(
                    subject=u"#carnival has {counter} photos".format(
                        counter=self.counter),
                    body=u"I'm awesome!",
                    from_email=u"Hashtag@EversnapApp.com",
                    to=("luisjarufe@gmail.com",),
                    cc=("davide@geteversnap.com",),
                    bcc=("davide@geteversnap.com",),
                )
                email.send()

    def get_conditions(self):
        conditions = ["#carnival", "filter:twimg"]
        if self.counter:
            last_creation_date = self.albums.order_by(
                "twitter_creation_date").last().twitter_creation_date
            conditions.append("since:{date}".format(
                date=last_creation_date.strftime("%Y-%m-%d")))

        return conditions

    def handle(self, *args, **options):
        twitter = TwitterConnector.objects.all().first()
        for result in twitter.get_results("#carnival", "filter:twimg"):
            if 'media' in result['entities']:
                for media in result['entities']['media']:
                    self._save(
                        user=result['user']['name'],
                        image_url=media['media_url'],
                        twitter_creation_date=result['created_at'],
                        favorite_count=result['favorite_count'])
            if 'retweeted_status' in result:
                if 'media' in result['retweeted_status']:
                    media_data = result['retweeted_status']['entities']['media']
                    for media in media_data:
                        self._save(
                            user=result['user']['name'],
                            image_url=media['media_url'],
                            twitter_creation_date=result['created_at'],
                            favorite_count=result['favorite_count'])
