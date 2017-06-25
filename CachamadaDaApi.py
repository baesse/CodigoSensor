import json, requests

i=0

while i < 10:


    response = requests.post("http://apitrivaga.azurewebsites.net/acheivaga/Estacionamento?codigodopiso=1&codigodavaga=10&desocupar=dasdsa")
    print(response.content)
    response = requests.get(
        "http://apitrivaga.azurewebsites.net/acheivaga/Estacionamento")
    print(response.content)
    response = requests.post(
        "http://apitrivaga.azurewebsites.net/acheivaga/Estacionamento?codigodopiso=1&codigodavaga=10")
    print(response.content)
    response = requests.get(
        "http://apitrivaga.azurewebsites.net/acheivaga/Estacionamento")
    print(response.content)
    i=i+1
