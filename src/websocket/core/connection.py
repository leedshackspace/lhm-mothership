from websocket.core.event_handler import AbstractEventHandler
from flask import request
import yaml


class ConnectionEventHandler(AbstractEventHandler):
    """ Handle Connection Events """

    def register_events(self):
        self.socket_io.on_event(
            "connect", self.on_connect)

    def on_connect(self):
        print("New Client Connected")
