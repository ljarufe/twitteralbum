import os
import urllib

from django import forms
from django.core.files import File

from dateutil.parser import parse

from albums.models import Album


class AlbumForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Album
        fields = ('user', 'image', 'image_url', 'twitter_creation_date',
                  'favorite_count')

    def __init__(self, *args, **kwargs):
        self.data['twitter_creation_date'] = parse(
            self.data['twitter_creation_date'])
        super(AlbumForm, self).__init__(*args, **kwargs)

    def clean_image_url(self):
        image_url = self.cleaned_data.get('image_url')
        if Album.objects.filter(image_url=image_url).exists():
            raise forms.ValidationError(u"This image already exists")

        return image_url

    def save(self, commit=True):
        obj = super(AlbumForm, self).super(commit=False)
        if self.image_url:
            result = urllib.urlretrieve(self.image_url)
            obj.image.save(
                os.path.basename(self.image_url), File(open(result[0])))
        if commit:
            obj.save()

        return obj
