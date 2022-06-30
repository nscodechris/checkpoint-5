import requests


def get_phone(name):
    name = name
    r = requests.get('http://localhost:5000/api?action=phone&name='+name)
    print(r.text)

def get_name(phone):
    phone = phone
    r = requests.get('http://localhost:5000/api?action=name&phone='+ phone)
    print(r.text)
