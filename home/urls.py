from django.conf.urls import url

from . import views
from django.contrib.auth import views as views_for_user

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^login/$', views_for_user.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', views_for_user.logout, {'template_name': 'logged_out.html'}, name='logout'),
]
