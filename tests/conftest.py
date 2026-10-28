import functools
import http.server
import pathlib
import threading

import pytest

from tests.pages.segment_page import SegmentPage

APP_DIR = pathlib.Path(__file__).resolve().parent.parent / "app"


@pytest.fixture(scope="session")
def base_url():
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(APP_DIR))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_port}"
    server.shutdown()


@pytest.fixture
def segment_page(page, base_url):
    segment_page = SegmentPage(page, base_url)
    segment_page.open()
    return segment_page
