import requests

# GET
response = requests.get('https://jsonplaceholder.typicode.com/posts')

print(response.status_code)
print(response.json())

# POST

body = {'title': 'test title',
        'body': 'test body',
        'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', body)

print(response.status_code)
print(response.json())

# PUT

body = {'title': 'test title edit',
        'body': 'test body edit',
        'userId': 1}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', body)

print(response.json())
print(response.status_code)

# PATCH

body = {'title': 'test title PATCH edit'}
response = requests.patch('https://jsonplaceholder.typicode.com/posts/1', body)

print(response.json())
print(response.status_code)