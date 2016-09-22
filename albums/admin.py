from django.contrib import admin

from albums.models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_url', 'creation_date',
                    'twitter_creation_date')
