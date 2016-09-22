from django.contrib import admin

from collector.models import TwitterConnector


@admin.register(TwitterConnector)
class TwitterConnectorAdmin(admin.ModelAdmin):
    list_display = ('token',)
