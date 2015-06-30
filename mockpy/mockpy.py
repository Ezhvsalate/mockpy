#!/usr/bin/env python

from utils import args_parser
from utils.network import NetworkConfig
from core.cherrypy_server import start_mock_server
from core.proxy_server import start_proxy_server
from utils.dir_init import *
from utils.config import *
import sys
import version
import os

def start():
    args = args_parser.parse()

    if args.version:
        print_version()

    if args.init:
        perform_init()

    if args.proxy:
        info("Enabling network proxy on {0}:{1}".format("127.0.0.1", args.port))

        warn("Note: sudo password may be asked to enable network http/https proxies\n")

        network = NetworkConfig(args.port)
        network.apply()

        print_environment(args)
        info("Starting proxy server")
        start_proxy_server(args.port, args.inout, args.res, network.previous_http_proxy)
    else:
        info("Starting mock server")
        print_environment(args)
        start_mock_server(args.port, args.inout, args.res)


def print_environment(args):
    path = os.popen("pwd").read().strip() + "/"
    info("Running with configuration:\n"
         "Input:'%s'\n" % (path + args.inout) +
         "Resources: '%s'\n" % (path + args.res))


def perform_init():
    current = os.popen("pwd").read().strip()
    dir_init = DirInit(current)
    dir_init.initialize()
    success("\nCurrent directory have been initialized successfully")
    info("\nTODO:\n1.Run 'mockpy'\n2.Visit http://localhost:9090/mockpy_hello_world to confirm mockpy is working")
    sys.exit(0)


def print_version():
    info(version.VERSION_STRING)
    sys.exit(0)
