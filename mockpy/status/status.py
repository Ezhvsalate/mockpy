import re
from mockpy.utils.log import *
from mockpy.utils import log


class Status(object):

    def __init__(self, mapping_handler):
        self.mapping_handler = mapping_handler

    def html_response(self):
        string = "<html>"
        string += "<body>"

        string += "Server running correctly<br/><br/>"
        string += "Parsed interceptors:<br/>"
        string += "_" * 80
        string += "<br/>"

        for item in self.mapping_handler.mappings:
            string += " - " + item.file_name + "<br/>"

            request = str(item.request).replace("\n", "<br/>")
            string += "<br/>"
            string += "Request:<br/>" + request + "<br/>"
            string += "<br/>"

            response = item.response.title()
            string += "Response:<br/>" + response + "<br/>"
            string += "_" * 80
            string += "<br/>"

        string += "</body>"
        string += "</html>"
        return string

    @staticmethod
    def is_status(url):
        is_status_url = re.match("^.*(127\.0\.0\.1|localhost|mockpy)(:\d*)?/status$", url) is not None

        if not is_status_url:
            is_status_url = re.match("^.*mockpystatus.com.*", url) is not None

        return is_status_url


def check_status_cherry_py(func):

    def parse_status(*args, **kwargs):
        self = args[0]

        if not hasattr(self, "status"):
            self.status = Status(self.mapping_handler)

        if self.status.is_status(self.cherrypy.url()):
            info("Accessing Status")
            log.print_seperator()
            return self.status.html_response()

        return func(self)

    return parse_status
