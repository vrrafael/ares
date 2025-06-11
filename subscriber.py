import json
import paho.mqtt.client as mqtt

from models import Log

topico = "topico"


def on_connect(client, userdata, flags, rc):
    print(f"Conectado! Código: {rc}")
    client.subscribe(topico)


def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico {msg.topic}")
    try:
        mensagem = json.loads(msg.payload.decode())
        Log.create(**mensagem)
        print("dados salvos na base de dados")
    except Exception as e:
        print(e)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883)
client.loop_forever()
