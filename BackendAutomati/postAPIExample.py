import requests
import json
from payload import *
import configparser
import requests
from utilities.configuration import *
from utilities.resources import *


addBook_response = requests.post(getConfig()['API']['endpoint'] +ApiResources.addBook,
                         json =addBookPayLoad("jlsfjljas"),)

print(addBook_response.json())
response_json  = addBook_response.json()
bookID = print(response_json['ID'])

#******Deleting the Added Book*********************d

response_deleteBook = requests.post(getConfig()['API']['endpoint'] +ApiResources.deleteBook,json = {
    "ID" : '"{}"'.format(bookID)
}, headers = {"Content-Type":"application/json"},)

assert response_deleteBook.status_code
print(response_deleteBook.status_code)
deletedbook = response_deleteBook.json()
print(type(deletedbook))
print(deletedbook['msg'])


assert deletedbook['msg'] == "book is successfully deleted"

#Authentication
url = "https://api.github.com/user"
github_response = requests.get(url,auth=('lavanyamantha',getpassword()))

print(github_response.status_code)