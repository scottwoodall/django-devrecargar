import os
import time

from django.conf import settings
from django.http import StreamingHttpResponse
from django.core.exceptions import ImproperlyConfigured

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

INIT_FILE = os.path.join(os.path.dirname(__file__), '__init__.py')

try:
    paths_to_watch = settings.DEVRECARGAR_PATHS_TO_WATCH
except AttributeError:
    try:
        paths_to_watch = [{'path': settings.BASE_DIR}]
    except AttributeError:
        message = """
            No paths were found for devrecargar to watch. See
            https://github.com/scottwoodall/django-devrecargar/blob/master/README.md
            for configuring this.
        """
        raise ImproperlyConfigured(message)


class EventHandler(PatternMatchingEventHandler):
    def on_modified(self, event):
        with open(INIT_FILE, 'a'):
            os.utime(INIT_FILE, None)

observer = Observer()

for path in paths_to_watch:
    event_handler = EventHandler(
        patterns=path.get('patterns', ['*.html', '*.js', '*.css']),
        ignore_directories=path.get('ignore_directories', True),
    )

    observer.schedule(
        event_handler,
        path['path'],
        recursive=path.get('recursive', True),
    )

observer.start()


def ping_generator():
    # function to hold the SSE connection open
    while True:
        yield time.time()
        time.sleep(30)


def ping(request):
    pings = (
        'retry:100\ndata:{"time":"%s"}\n\n' % ping
        for ping in ping_generator()
    )

    response = StreamingHttpResponse(
        (ping for ping in pings),
        content_type="text/event-stream"
    )

    return response
