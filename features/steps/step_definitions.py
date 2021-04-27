import requests
from behave import *

api_url = None


@given('user sets API URL')
def setup_endpoint(context):
    global api_url
    api_url = 'https://jsonplaceholder.typicode.com/'
