#!/usr/bin/env python
import yaml
from Unifi import Unifi

with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

unifi = Unifi.login(cfg['unifi'])

r = unifi.get_clients()
clients = r.json()
unifi.logout()

print(clients["data"])
