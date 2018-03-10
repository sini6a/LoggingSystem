from django.conf.urls import url

from . import views
from django.contrib.auth import views as views_for_user

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^login/$', views_for_user.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', views_for_user.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^logs/easteregg/$', views.signup),
    url(r'^update_profile/$', views.update_profile, name='update_profile'),
    url(r'^profile/$', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
