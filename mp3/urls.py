from django.conf.urls import url
from . import views

app_name = 'mp3'

urlpatterns = [
    #/mp3/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/mp3/PK/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #mp3/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    #mp3/album/pk/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    #mp3/album/pk/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]
