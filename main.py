import os
import requests
import json
import threading
interval = 300

boletos = os.environ.get('BOLETOS')


def send_message(text):
    print("Sending message: {}".format(text))
    url = "https://api.telegram.org/bot{}/sendMessage".format(os.environ.get('TELEGRAM_TOKEN'))
    params = {'chat_id': os.environ.get('CHAT_ID'), 'text': text}
    requests.post(url, data=params)


if boletos is None:
    print('No se encontraron boletos')
    exit()
else:
    print('Boletos: ' + boletos)

premiados = {}


def check_premiados():
    for boleto in boletos.split(','):
        if boleto in premiados:
            continue
        r = requests.get('https://api.elpais.com/ws/LoteriaNavidadPremiados?n=' + boleto)
        if r.status_code == 200:
            json_text = r.text.split("=")[1]
            response = json.JSONDecoder().decode(json_text)

            if 'error' in response and response['error'] != 0:
                print("Error consultando el boleto {}".format(boleto))
                print(json_text)
                continue

            premiados[boleto] = response['premio']
            if response['premio'] > 0:
                send_message('Boleto ' + boleto + ' premiado con ' + str(response['premio']) + ' € el décimo')
            elif response['premio'] == 0:
                send_message('Boleto ' + boleto + ' no premiado')
        else:
            print('Error al obtener premio de ' + boleto)

    print('Premiados:')
    for premiado in premiados:
        print(premiado + ': ' + str(premiados[premiado]))


def start_timer():
    threading.Timer(interval, start_timer).start()
    check_premiados()


start_timer()
