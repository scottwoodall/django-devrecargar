from django.conf.urls import url

from .views import ping

app_name = 'devrecargar'

urlpatterns = [
    url(r'^ping/', ping, name='ping'),
]
