import requests


class Unifi:
    """Client to the Unifi Controller"""

    def __init__(self, url, site, session):
        self.url = url
        self.session = session
        self.api = url + "/api/s/" + site

    def login(config):
        url = config["url"]

        s = requests.session()
        auth = {"username": config["user"], "password": config["passwd"]}
        s.post(url + "/api/login", json=auth, verify=False)
        return Unifi(url, config["site"], s)

    def logout(self):
        return self.session.get(self.url + "/api/logout", verify=False)

    def get_clients(self):
        return self.session.get(self.api + "/rest/user", verify=False)

