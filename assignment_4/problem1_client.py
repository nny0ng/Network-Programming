import requests

data = input("put the keyword: ") # inout keyword
r = requests.get('http://127.0.0.1:8000/', params=data) # send to server

print('=>', r.text) # print server's response