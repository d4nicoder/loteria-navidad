# Notificación de lotería de navidad

Este es un pequeño script que te notificará por Telegram si algún boleto de lotería de navidad que hayas proporcionado en las variables de entorno ha sido premiado y con cuanto importe.

Cada 5 minutos se conecta a la API de [elpais.com](https://servicios.elpais.com/sorteos/loteria-navidad/api/) y verificará tus números. En caso de que alguno haya sido premiado, si no se había notificado previamente, se enviará un mensaje con el premio obtenido por décimo.

## Como usarlo

Para ejecutar el script necesitamos tener instalado python 2.7.x o 3.x y el paquete [requests](https://pypi.python.org/pypi/requests).

Podemos instalar el paquete de la siguiente manera:
```bash
pip install requests
```

Para el correcto funcionamiento debemos declarar las siguientes variables de entorno:
```bash
PYTHONUNBUFFERED=1
BOLETOS=<lista_separada_por_comas>
TELEGRAM_TOKEN=<token>
CHAT_ID=<chat_id>
```

### Ejemplo:
```bash
PYTHONUNBUFFERED=1 BOLETOS=12345,67890 TELEGRAM_TOKEN=MySuperSecretTokenCHAT_ID=-1234567 pyhton main.py
```

### Docker:

También puedes usar la imagen de docker alojada en Dockerhub:
```bash
docker run --rm \
  --env PYTHONUNBUFFERED=1 \
  --env BOLETOS=12345,67890 \
  --env TELEGRAM_TOKEN=MySuperSecretToken \
  --env CHAT_ID=-1234567 \
  danitetus/loteria-navidad:latest
```
## Disclaimer
Este script obtiene los datos de una api pública de [elpais.com](https://servicios.elpais.com/sorteos/loteria-navidad/api/), ya que la fuente oficia no proporciona ninguna API de la que extraer información. Al no tratarse ElPais de una fuente oficial, es posible que los datos no sean del todo correctos. Verifica siempre los datos en la página oficial de [Loterías y apuestas del Estado](https://www.loteriasyapuestas.es/es) 
