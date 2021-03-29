import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'RahulShetty'},)
#print(response.text)
#print(type(response.text))

#dict_response = json.loads(response.text)
#print(type(dict_response))
#print(dict_response[0]['isbn'])

json_response = response.json()
print(json_response[0]['isbn'])
print(response.status_code)
assert response.status_code == 200
print(response.headers)

#Retrive the bookdetails with isbn = 'RA'
response_data = response.json()
for actualbook in response_data:
    print(type(actualbook))
    if actualbook['isbn'] == 'RA':
        print(actualbook)
        break

expectedBook = {
        "book_name": "RestAssured",
        "isbn": "RA",
        "aisle": "1001"
    }

assert  actualbook == expectedBook