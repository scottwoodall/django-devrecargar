# django-devrecargar #
During the development of a Django application, do you get tired of:

1. Making a change to source code
1. Alt-tab to your browser
1. Refresh
1. Rinse and repeat

This project aims to make you more productive by keeping you in the text editor by automatically refreshing the browser after any file modification within your Django project (even CSS, JS or HTML).

### Installation ###
`pip install django-devrecargar`

### Usage ###

1. Add `devrecargar` to your `INSTALLED_APPS` in `settings.py`
1. Add an entry to your `urls.py`:
    ```url(r'^devrecargar/', include('devrecargar.urls', namespace='devrecargar'))```
1. Add a javascript snippet to your base template:
    ```<script>{% include "devrecargar/devrecargar.js" %}</script>```
    
### How It Works ###
The javascript snippet makes a Server-Sent Event (SSE) request to the Django devserver. Anytime the devserver process restarts the SSE request is disconnected within the browser and it will automatically try to reconnect natively. SSE will send an `open` event after it reconnects once the devserver has been restarted.  We listen for that `open` event and issue a `location.reload()` that refreshes the browser.

After modifying a python file the devserver restarts automatically.  To get CSS, JS, HTML support we use the `watchdog` module to listen for any file modifications. When a `watchdog` modification event happens an `__init__.py` file within the Django project is "touched" which the devserver process notices because it's a python file and restarts itself, which triggers the SSE `open` event to fire.

### How can I keep this out of my production environment?
* In the HTML template wrap the javascript snippet in a `debug` conditional. 
	* ```{% if debug %}<script>{% include "devrecargar/devrecargar.js" %}</script>{% endif %}```
	* You need `django.template.context_processors.debug` added to `TEMPLATE_CONTEXT_PROCESSORS` in `settings.py`. If you don't have a `TEMPLATE_CONTEXT_PROCESSORS` then the [Django default configuration includes it](https://docs.djangoproject.com/en/1.9/ref/settings/#template-context-processors).
	* Be sure your IP address is listed in `INTERNAL_IPS ` within `settings.py`
* In `urls.py` only add the route if `DEBUG=True`

        urlpatterns = []
        if settings.DEBUG:
            urlpatterns.append(
                url(r'^devrecargar/', include('devrecargar.urls', namespace='devrecargar')
            )
        )
    
### Why devrecargar over other solutions?
1. Python only
1. No browser plugins
1. Easier for remote workflows where you are SSH'ed into a development server making changes but viewing the site with a browser on your local PC.

### Where does the name devrecargar come from?
Recargar is Spanish for "reload".
