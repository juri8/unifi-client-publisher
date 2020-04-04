#!/usr/bin/env python3
import yaml
from Unifi import Unifi
import paho.mqtt.client as mqtt

with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

def get_mqtt(config):
    client = mqtt.Client()
    if("user" in config):
        client.username_pw_set(config['user'], config['passwd'])
    client.connect(config['host'])

unifi = Unifi.login(cfg['unifi'])
r = unifi.get_clients()
clients = r.json()
unifi.logout()

# mqtt_client = get_mqtt(cfg['mqtt'])
# mqtt_client.publish()


for entry in clients['data']:
    print(entry)
