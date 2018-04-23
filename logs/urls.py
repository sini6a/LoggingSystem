from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='logs'),
	url(r'^(?P<log_id>[0-9]+)/$', views.log),
    url(r'^(?P<log_id>[0-9]+)/delete/$', views.delete),
    url(r'^search/$', views.search),
]
