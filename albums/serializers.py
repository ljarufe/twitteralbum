from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('user', 'image', 'image_url', 'twitter_creation_date',
                  'creation_date', 'favorite_count')
