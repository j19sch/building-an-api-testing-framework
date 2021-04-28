import requests

def printResponse(funcName, response):
    print(f"[{funcName}] Status: {response.status_code}")
    print(f"[{funcName}] Response: {response.text}")


def getKnockknockRequest():
    response = requests.get('http://localhost:8000/knockknock')
    printResponse(getKnockknockRequest.__name__, response)


def getBooksRequest():
    response = requests.get('http://localhost:8000/books')
    printResponse(getBooksRequest.__name__, response)


def getBookRequest():
    response = requests.get(
        'http://localhost:8000/books/9b30d321-d242-444f-b2db-884d04a4d806')
    printResponse(getBookRequest.__name__, response)


def postBookRequest():
    payload = {
        'title': 'New book',
        'sub_title': 'New book sub title',
        'author': 'Dmytro Titenko',
        'publisher': 'Mendix',
        'year': 2021,
        'pages': 53
    }
    response = requests.post('http://localhost:8000/books', json=payload)
    printResponse(postBookRequest.__name__, response)

def postTokenRequest():
    response = requests.post('http://localhost:8000/token/Dmytro.Titenko')
    printResponse(postTokenRequest.__name__, response)


getKnockknockRequest()
getBooksRequest()
getBookRequest()
postBookRequest()
postTokenRequest()
