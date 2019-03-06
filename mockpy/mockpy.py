#!/usr/bin/env python

import os
import sys

from colorama import init as colorama_init

from .core.cherrypy_server import start_mock_server
from .utils import args_parser
from .utils.dir_init import *
from .version import *


def start():
    colorama_init()
    args = args_parser.parse()

    if args.version:
        print_version()

    if args.init:
        perform_init()

    info("Starting mock server")
    print_environment(args)
    start_mock_server(args.port, args.inout, args.res, args.delay)


def print_environment(args):
    path = os.getcwd().strip() + os.sep
    info("Running with configuration:\n"
         "Input:'%s'\n" % (path + args.inout) +
         "Resources: '%s'\n" % (path + args.res))


def perform_init():
    current = os.getcwd().strip()
    dir_init = DirInit(current)
    dir_init.initialize()
    success("\nCurrent directory have been initialized successfully")
    info("\nTODO:\n1.Run 'mockpy'\n2.Visit http://localhost:9090/mockpy_hello_world to confirm mockpy is working")
    sys.exit(0)


def print_version():
    info(VERSION_STRING)
    sys.exit(0)
