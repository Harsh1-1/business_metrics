from api import app
from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

dispatcher = DispatcherMiddleware(app, {'/metrics': make_wsgi_app()})
if __name__ == "__main__":
    run_simple(hostname="0.0.0.0", port=8659, application=dispatcher)
