import time
import os

from django.conf import settings
from django.http import StreamingHttpResponse

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


class EventHandler(PatternMatchingEventHandler):
    def on_modified(self, event):
        init_file = os.path.join(settings.BASE_DIR, '__init__.py')

        with open(init_file, 'a'):
            os.utime(init_file, None)

event_handler = EventHandler(
    patterns=['*.html', '*.js', '*.css'],
    ignore_directories=True,
)

observer = Observer()
observer.schedule(event_handler, settings.BASE_DIR, recursive=True)
observer.start()


def ping_generator():
    while True:
        yield time.time()
        time.sleep(30)


def ping(request):
    rows = (
        'retry:100\ndata:{"ping":"%s"}\n\n' % ping
        for ping in ping_generator()
    )

    response = StreamingHttpResponse(
        (row for row in rows),
        content_type="text/event-stream"
    )

    return response
