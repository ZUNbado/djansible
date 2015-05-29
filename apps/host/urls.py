from django.conf.urls import patterns, include, url

from .views import HostView, InventoryView

urlpatterns = patterns('',
        url(r'^host/?$', HostView.as_view()),
        url(r'^host/(?P<host_id>[0-9]+)/?$', HostView.as_view()),
        url(r'^inventory/?$', InventoryView.as_view()),
    )
