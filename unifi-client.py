#!/usr/bin/env python

import yaml
import requests

with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

config = cfg["unifi"]
url = config["url"]
api = url + "/api/s/" + config["site"]

s = requests.session()


def login():
    auth = {"username": config["user"], "password": config["passwd"]}
    return s.post(url + "/api/login", json=auth, verify=False)


def logout():
    return s.get(url + "/api/logout", verify=False)


def get_clients():
    return s.get(api + "/rest/user", verify=False)


login()
# TODO: verify success
r = get_clients()
clients = r.json()
logout()

print(clients["data"])
