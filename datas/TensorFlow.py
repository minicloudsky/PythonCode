
# -*- coding: utf-8 -*-

import json
from six.moves import urllib


def application(environ, start_response):
    # print(environ)
    status = '200 OK'
    headers = [('Content-Type', 'text/html; charset=utf8')]
    get_arguments = urllib.parse.parse_qs(environ['QUERY_STRING'])
    args_dict = {k: v[0] for k, v in get_arguments.items()}
    start_response(status, headers)
    return json.dumps(args_dict)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('127.0.0.1', 8889, application)
    httpd.serve_forever()