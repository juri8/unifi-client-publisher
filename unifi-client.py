#!/usr/bin/env python3
import yaml
from Unifi import Unifi
import paho.mqtt.publish as publish

with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

unifi = Unifi.login(cfg['unifi'])
r = unifi.get_clients()
clients = r.json()
unifi.logout()

mqtt_config = cfg['mqtt']

baseTopic = mqtt_config['baseTopic']
msgs = []
for entry in clients['data']:
    # print(entry)
    device_topic = baseTopic + entry['mac'] + "/"
    msgs.append((device_topic + "name", entry['hostname']))
    msgs.append((device_topic + "last_seen", entry['last_seen']))

mqtt_auth = {
    'username': mqtt_config['user'],
    'password': mqtt_config['passwd']
}
publish.multiple(msgs, mqtt_config['host'], auth = mqtt_auth)