import json
from urllib.parse import parse_qs

import app.utils as utils


def sum_of_two(environ, start_response):
    params = parse_qs(environ.get('QUERY_STRING', ''))
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'application/json'),
    ]

    arr = list(map(int, params.get('arr', [])))
    response = {
        'sum_of_two': utils.sum_of_two(arr)
    }

    start_response(status, response_headers)
    return [json.dumps(response).encode('utf-8')]


def paired_with_dict(environ, start_response):
    if environ['REQUEST_METHOD'] == 'POST':
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except ValueError:
            request_body_size = 0

        request_body = environ['wsgi.input'].read(request_body_size)
        response = 'Post data'
    else:
        response = 'Get data'

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/json'),
    ]
    start_response(status, response_headers)
    return [json.dumps(response).encode('utf-8')]


routes = {
    '/sum_of_two': sum_of_two,
    '/paired_with_dict': paired_with_dict,
}


class Application:
    def __init__(self, routes):
        self.routes = routes

    def not_found(self, environ, start_response):
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return ['404 Not Found']

    def __call__(self, environ, start_response):
        handler = self.routes.get(environ.get('PATH_INFO', '').rstrip('/')) or self.not_found
        return handler(environ, start_response)


app = Application(routes)
