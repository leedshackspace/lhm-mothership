import yaml
from flask import request


class AbstractEventHandler(object):
    WEBSOCKET_API_CONFIG_LOCATION = "./config/api_keys/websocket.yaml"

    def __init__(self, socket_io=None):
        self.socket_io = socket_io
        self.api_keys = self.load_config()
        self.register_events()

    def load_config(self):
        """ Loads the API Key configuration for Websocket authentication """
        config = {}
        with open(self.WEBSOCKET_API_CONFIG_LOCATION, "r") as config_file:
            parsed_config = yaml.safe_load(config_file)
            for _, item in parsed_config.items():
                api_key = item.get("key")
                status = item.get("status")
                application = item.get("application")
                config[api_key] = {"status": status,
                                   "application": application}
        return config

    def is_authorised(self, message):
        api_key = message.get("api_key")
        if not api_key:
            print("Not Supplied")  # TODO: What if key isn't supplied?
        if api_key not in self.api_keys:
            print("Unauthorised")  # TODO: Unauthorised logic
        key_details = self.api_keys.get(api_key)
        status = key_details.get("status")
        if status == 0:
            request._HSMANAGEMENT_STAGING = False
            pass
        elif status == 1:
            request._HSMANAGEMENT_STAGING = True
            pass
        elif status == 2:
            # TODO: Not Active Logic, Contact Hackspace directors and/or Tom
            pass
        elif status == 3:
            # TODO: Access Revoked Logic, this is more of a "nope, not allowed here"
            pass

    @property
    def ws(self):
        if (self.socket_io is None):
            raise NotImplementedError(
                "The SocketIO object was not passed to the Event Handler.")
        else:
            return self.socket_io

    @staticmethod
    def register_events():
        raise NotImplementedError(
            "You must override the register_events method.")
