from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new_log/$', views.new_log, name='new_log'),
    url(r'^list_logs/$', views.list_logs, name='list_logs'),
    url(r'^(?P<log_id>[0-9]+)/$', views.single_log),
    url(r'^(?P<log_id>[0-9]+)/delete/$', views.delete),
    url(r'^(?P<log_id>[0-9]+)/modify/$', views.modify),
    url(r'^search/$', views.search),
    url(r'^backup/$', views.backup, name='backup_logs'),
]
