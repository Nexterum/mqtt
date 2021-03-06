import paho.mqtt.client as mqtt
import schedule
import time


# The callback for when the client receives a CONNACK response from the server.
def on_connect(cl, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    cl.subscribe("/medvedkovo/big_room")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def on_event():
    print('12345678')


schedule.every(3).seconds.do(on_event)

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set('server', '3da3d15123')

client.connect("mqtt.sonys.ru", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()


