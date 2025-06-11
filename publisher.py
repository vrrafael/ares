from datetime import datetime
from itertools import count
import json
import random
import time

import paho.mqtt.client as mqtt

broker = "127.0.0.1"
port = 1883
topico = "topico"
device_mac = "b8:27:eb:45:12:34"


def on_connect(client, userdata, flags, rc):
    print(f"Conectado ao broker com código {rc}")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.connect(broker, port)

for i in count():
    mensagem = {
        "device_id": device_mac,
        "temperatura": f"{round(random.uniform(23, 23.5), 2)}°C",
        "umidade": f"{round(random.uniform(70, 72), 2)}%",
        "dt_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    client.publish(topico, json.dumps(mensagem))
    print(f"Publicado: {mensagem}")
    time.sleep(3)

client.disconnect()
