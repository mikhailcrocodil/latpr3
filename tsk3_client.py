import requests

s = requests.Session()

def authentication(username, password):
    url = 'http://127.0.0.1:5000/'
    params = {
        'username': username,
        'password': password
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return "1"
    else:
        return response.json()['msg']


def try_auth(username, password):
    result = authentication(username, password)
    if result == "1":
        print(f'Пароль {username}: ' + password)
    else:
        print(result)

try_auth('mikhail', 'password')
try_auth('mikhail', 'qwerty')
try_auth('mikhail', 'mikhail')
try_auth('mikhail', 'rtumirea')
try_auth('mikhail', 'password')

