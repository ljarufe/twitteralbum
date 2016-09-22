from django.shortcuts import render

from rest_framework import viewsets

from .serializers import AlbumSerializer
from .models import Album


def album(request):
    albums = Album.objects.all()

    return render(request, "albums/album.html", dict(albums=albums))


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
