from django.conf.urls import url

from . import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.index),
    
]
