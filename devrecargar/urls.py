from django.conf.urls import url

from .views import ping

urlpatterns = [
    url(r'^ping/', ping, name='ping'),
]
