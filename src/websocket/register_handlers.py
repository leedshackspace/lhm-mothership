from websocket.openbot import EntryEventHandler
from websocket.core import ConnectionEventHandler


def register_handlers(socket_io):
    socket_io = ConnectionEventHandler(socket_io).ws
    socket_io = EntryEventHandler(socket_io).ws
    return socket_io
