from core.constants.redis.databases import RedisDatabases
from core.constants.config import Config
from uuid import uuid4
import redis
import json

class OpenBotRedisInteraction():
    def __init__(self):
        config = Config().core.get("redis")        
        self.r = redis.StrictRedis(
            port=config.get("port"),
            password=config.get("password"),
            host=config.get("host"),
            db=RedisDatabases.OPENBOT_TRIGGERS)

    def new_entry(self, socket_id=None):
        if socket_id is None:
            # TODO: Proper exception
            raise Exception("Need a socket ID please :)")
        uid = uuid4().hex
        self.r.set(uid, socket_id, ex=180)
        return uid
