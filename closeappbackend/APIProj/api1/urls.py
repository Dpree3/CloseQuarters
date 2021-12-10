
from django.urls import path
from .views import NbaList,NflList,NcaaList

from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('NBA', NbaList),
    path('NFL', NflList),
    path('NCAA', NcaaList),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


]