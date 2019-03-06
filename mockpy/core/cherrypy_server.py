import signal

import cherrypy
import socket

from mockpy.models.mapping_items_manager import *
from mockpy.utils.config import *
from .cherrypy_mapper import *


class CherryPyServer(object):
    exposed = True

    def __init__(self, inout_path, res_path, delay):
        self.handler = MappingItemsManager(inout_path, res_path)
        success("Server started successfully at %s:%s" %
                ("http://" + socket.gethostbyname(socket.gethostname()), cherrypy.config["server.socket_port"]))
        self.delay = delay

    @cherrypy.expose
    def default(self, *args, **kwargs):
        mapper = CherryPyMapper(mapping_handler=self.handler, cherrypy=cherrypy, delay=self.delay)
        return mapper.handle_request(delay=self.delay)


def start_mock_server(port, inout_path, res_path, delay):
    cherrypy.config.update({'server.socket_port': port, "environment": "embedded"})
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})

    def signal_handler(signal, frame):
        info("\nShutting down server")
        cherrypy.engine.exit()
        success("Server shutdown successfully")

    signal.signal(signal.SIGINT, signal_handler)
    cherrypy.quickstart(CherryPyServer(inout_path, res_path, delay))
