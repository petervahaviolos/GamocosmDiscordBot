import requests, json
from enum import Enum

class Endpoint(Enum):
    START_SERVER = "start"
    STOP_SERVER = "stop"
    REBOOT_SERVER = "reboot"
    START_MINECRAFT = "resume"
    STOP_MINECRAFT = "pause"
    STATUS = "status"
    SEND_COMMAND = "exec"

class Server:
    def __init__(self, server_id:str, api_key:str):
        self.server_id = server_id
        self.api_key = api_key
        self.base_url = "https://gamocosm.com/servers/"
        self.api_url = f"{self.base_url}{self.server_id}/api/{self.api_key}/"

    def _get(self, endpoint:Endpoint):
        """Send a GET request to endpoint and return the JSON parsed response"""
        response = requests.get(self.api_url + endpoint.value)
        return self._parse(response)

    def _post(self, endpoint:Endpoint, data:dict=""):
        """Send a POST request to endpoint with data and return the response"""
        response = requests.post(self.api_url + endpoint.value, data=data)
        return response

    def _parse(self, response):
        """Return the JSON parsed response"""
        return json.loads(response.text)

    def _status(self):
        """Return the JSON response of the server status"""
        return self._get(Endpoint.STATUS)

    def server_start(self):
        """Send a POST request to start the server and return the JSON parsed response"""
        return self._post(Endpoint.START_SERVER)

    def server_stop(self):
        """Send a POST request to stop the server and return the JSON parsed response"""
        return self._post(Endpoint.STOP_SERVER)

    def server_reboot(self):
        """Send a POST request to reboot the server and return the JSON parsed response"""
        return self._post(Endpoint.REBOOT_SERVER)

    def minecraft_start(self):
        """Send a POST request to start the minecraft server and return the JSON parsed response"""
        return self._post(Endpoint.START_MINECRAFT)

    def minecraft_stop(self):
        """Send a POST request to stop the minecraft server and return the JSON parsed response"""
        return self._post(Endpoint.STOP_MINECRAFT)

    def server_online(self):
        """Send a GET request to the server status endpoint and return the state of the server"""
        return "online" if self._get(Endpoint.STATUS)['server'] else "offline"

    def minecraft_online(self):
        """Send a GET request to the server status endpoint and return the state of the minecraft server"""
        return "online" if self._get(Endpoint.STATUS)['minecraft'] else "offline"

    def pending_state(self):
        """Send a GET request to the server status endpoint and return the pending state of the server"""
        return "active" if self._get(Endpoint.STATUS)['status'] is None else self._get(Endpoint.STATUS)['status']

    def ip_address(self):
        """Send a GET request to the server status endpoint and return the ip address of the server"""
        return self._get(Endpoint.STATUS)['ip']

    def domain(self):
        """Send a GET request to the server status endpoint and return the domain of the server"""
        return self._get(Endpoint.STATUS)['domain']

    def download(self):
        """Send a GET request to the server status endpoint and return and return a URL to download the minecraft server world"""
        return self._get(Endpoint.STATUS)['download']

    def send_command(self, command:str):
        """Send command to the minecraft server"""
        return self._post(Endpoint.SEND_COMMAND, {'command': command})
