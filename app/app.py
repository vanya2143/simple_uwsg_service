import json
import re

import app.utils as utils
from urllib.parse import parse_qs


def index(environ, start_response):
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
    ]
    start_response(status, response_headers)
    return ['Hello'.encode('utf-8')]


def sum_of_two(environ, start_response):
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'application/json'),
    ]

    arr = list(map(int, parameters.get('arr', [])))
    result = utils.sum_of_two(arr)

    response = {
        'sum_of_two': result
    }

    start_response(status, response_headers)
    return [json.dumps(response).encode('utf-8')]


def paired_with_dict(environ, start_response):
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
    ]
    start_response(status, response_headers)
    return [environ.get('QUERY_STRING', '').encode('utf-8'), environ.get('RAW_URI', '').encode('utf-8')]


urls = [
    # (r'^$', index),
    (r'sum_of_two/?$', sum_of_two),
    (r'paired_with_dict/?$', paired_with_dict)
]


def not_found(environ, start_response):
    status = '404 NOT FOUND '
    response_headers = [
        ('Content-Type', 'text/plain'),
    ]
    start_response(status, response_headers)
    return ['not found'.encode('utf-8')]


def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path)
        if match is not None:
            return callback(environ, start_response)
    return not_found(environ, start_response)


# uwsgi --socket 127.0.0.1:8080 --protocol=http --wsgi-file app/app.py
