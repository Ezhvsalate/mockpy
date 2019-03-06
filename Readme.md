# Mockpy

Fork of Mockpy - a python command line utility to create development mock servers.  
Mockpy works by reading a list of configuration files in the YAML format, it uses these configurations to match the HTTP request received and return an http response based on the matched YAML file configuration.

# What is changed in this fork?
 - functionality of creating proxy for OS-X is cut away
 - creation of standalone web server works in Windows and *nix
 - Python3 compatible
 - Additional command line parameters
 
# Why mockpy
- You want a very lightweight utility to quickly create a mock API
- Update to the mock API are picked up from files without the need to start/restart the server again.

# Installation

This fork can be installed directly from github repo:

`pip install https://github.com/Ezhvsalate/mockpy/archive/master.zip`

# Usage

Bellow is a description of the basic operations that `mockpy` provides, for a more comprehensive list, please refer to [the wikis](https://github.com/oarrabi/mockpy/wiki).

## Initialize a directory
Initialize a the current folder by running:

    mockpy init
This will create two folders:    

`inout`: this folder will contains a list of mapping YAML files, each YAML file represents an request and response operation.

`res`: resource folder contains the static HTML, JSON, Images and static files returned as part of the mocking process.

To understand the YAML file format, please refer to the documentation.

### Sample 

    request:
        method: GET
        url: .*sample/matching.*
    response:
        status: 200
        body: hello world

The above catches all the GET request that has `sample/matching` in its URL, and returns the status 200. 
Requesting `http://localhost:9090/sample/matching` returns a response with `"hello world"` in its body.       
        
    request:
        method: POST
        url: .*/api/cats/search.*
        body: .*greyCat.*
    response:
        status: 200
        body_file: grey_cats_list.json
        headers:
            application/json

This one catches all the POST request that has `/api/cats/search` in its URL, `greycat` in body and returns the status 200. 
It returns a response with contents of file `grey_cats_list.json` in its body.

More information about the YAML request/response check out the [wikis](https://github.com/oarrabi/mockpy/wiki/YAML-request-response--file-format).

## Start the mock server
The mock server can be started as a standalone web server.
Use `mockpy start` to start the standalone web server, this will setup a server on the default port. 
Visit `127.0.0.1:9090` to check the mock server.
