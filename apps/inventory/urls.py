from django.conf.urls import patterns, include, url

from .views import HostRedirView, InventoryView

urlpatterns = patterns('',
        url(r'^check/(?P<host_name>.*)', HostRedirView.as_view()),
        url(r'^view', InventoryView.as_view())
        )
