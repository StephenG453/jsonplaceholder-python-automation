import requests
from behave import *

api_endpoints = {}
api_url = None

post_request_body = {}

response_id = None


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


@step('user sends a valid POST http request')
def add_post(context):
    response = requests.post('https://jsonplaceholder.typicode.com/posts', post_request_body)

    global response_id
    response_id = response.json()['id']

    assert response.status_code == 201


@step('user gets the created entity')
def get_entity(context):
    # would use response_id but its not actually created, so we will get 404
    # global response_id

    response = requests.get('https://jsonplaceholder.typicode.com/posts/' + str(1))

    assert response.status_code == 200


@step('user deleted the created entity')
def get_entity(context):

