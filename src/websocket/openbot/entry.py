from flask_socketio import SocketIO, emit
from core.constants.websockets import OpenBotEvents
from websocket.core.event_handler import AbstractEventHandler
from core.redis.openbot.spy import OpenBotExpirySpy
from core.redis.openbot.interaction import OpenBotRedisInteraction
from flask import request


class EntryEventHandler(AbstractEventHandler):
    def register_events(self):
        self.socket_io.on_event(
            OpenBotEvents.MANUAL_TRIGGER, self.manual_trigger)
        self.redis = OpenBotRedisInteraction()
        spy = OpenBotExpirySpy()
        spy.callback = self.on_expire

    def manual_trigger(self, message):
        self.is_authorised(message)
        uid = self.redis.new_entry(socket_id=request.sid)

    def on_expire(self, message):
        print("Expired")
