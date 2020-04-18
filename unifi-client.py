#!/usr/bin/env python3
import sys

import yaml
from Unifi import Unifi
import paho.mqtt.publish as publish

with open(sys.path[0] + "/config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

unifi = Unifi.login(cfg['unifi'])
r = unifi.get_clients()
clients = r.json()
r = unifi.get_clientstats()
client_stats = r.json()
unifi.logout()

mqtt_config = cfg['mqtt']

client_stats0 = {}

for entry in client_stats['data']:
    client_stats0[entry['mac']] = entry

baseTopic = mqtt_config['baseTopic']
msgs = []
for entry in clients['data']:
    # print(entry)
    device_topic = baseTopic + entry['hostname'] + "/"
    if entry['mac'] in client_stats0:
        status = 'ONLINE'
    else:
        status = 'OFFLINE'

    msgs.append((device_topic + "status", status))
    # msgs.append((device_topic + "last_seen", entry['last_seen']))

mqtt_auth = {
    'username': mqtt_config['user'],
    'password': mqtt_config['passwd']
}
publish.multiple(msgs, mqtt_config['host'], auth = mqtt_auth)