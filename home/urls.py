from django.conf.urls import url

from . import views
from django.contrib.auth import views as views_for_user

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^login/$', views_for_user.login, {'template_name': 'profile_login.html'}, name='account_login'),
    url(r'^logout/$', views_for_user.logout, {'template_name': 'profile_logged_out.html'}, name='account_logout'),
    url(r'^logs/easteregg/$', views.signup),
    url(r'^update_profile/$', views.update_profile, name='account_update'),
    url(r'^profile/$', views.profile, name='account_info'),
    url(r'^about_us/$', views.about_us, name='about_us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
