import requests
from behave import *

api_endpoints = {}
api_url = None

post_request_body = {}


@given('user sets API URL')
def set_url(context):
    global api_url
    api_url = 'https://jsonplaceholder.typicode.com'


@given('user sets posts endpoint')
def set_posts_endpoint(context):
    api_endpoints['POSTS_URL'] = api_url + '/posts'


@when('user defines post request body')
def define_post_body(context):
    global post_request_body
    for row in context.table:
        post_request_body = {'title': row['title'],
                             'body': row['body'],
                             'userId': row['userid']}


@when('user sends a valid post http request')
def add_post(context):
    response = requests.post('https://jsonplaceholder.typicode.com/posts', post_request_body)

    assert response.status_code == 201
