from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'get_album', views.AlbumViewSet)

urlpatterns = [
    url(r'^api/',
        include(router.urls)),
    url(r'^album/',
        views.album,
        name='album'),
]
