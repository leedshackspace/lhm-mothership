#! venv/bin/python

from flask import Flask
from core.datastore.models.member.Interface import MemberInterface
from views.register_routes import register_routes
from websocket.register_handlers import register_handlers
from flask_socketio import SocketIO


class Application(object):
    app = None

    def __init__(self, name):

        self.flask_app = Flask(name)
        self.flask_app.config["SECRET_KEY"] = "shhh"

        self.flask_app = register_routes(self.flask_app)
        MemberInterface()
        self.socket_io = SocketIO(self.flask_app)
        register_handlers(self.socket_io)

    def run(self):
        self.socket_io.run(self.flask_app, debug=True)


if __name__ == "__main__":
    app = Application("HS-Management")
    app.run()
