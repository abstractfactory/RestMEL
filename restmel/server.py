# Standard library
import threading

# Dependencies
import requests
import flask
import flask.ext.restful

# Local library
import rest

app = flask.Flask(__name__)
api = flask.ext.restful.Api(app)

api.add_resource(rest.Node, "/node")
api.add_resource(rest.Command, "/command")

PORT = 6000


def start(port=None, safe=False):
    """Start server

    Arguments:
        safe (bool): Ensure there is no existing server already running

    """

    if safe:
        try:
            stop()
        except:
            pass

    if port:
        global PORT
        PORT = port

    def run():
        app.run(port=PORT)

    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    print "Running Flask server @ port %i.." % PORT


def stop():
    requests.get("http://127.0.0.1:%i/shutdown" % PORT)


def restart():
    stop()
    start()


def _shutdown_server():
    """Shutdown the currently running server"""
    func = flask.request.environ.get("werkzeug.server.shutdown")
    if func is not None:
        func()


@app.route("/shutdown", methods=["POST"])
def _shutdown():
    """Shutdown server

    Utility endpoint for remotely shutting down server.

    Usage:
        $ curl -X GET http://127.0.0.1:6000/shutdown

    """

    print "Server shutting down..."
    _shutdown_server()
    print "Server stopped"
    return True
