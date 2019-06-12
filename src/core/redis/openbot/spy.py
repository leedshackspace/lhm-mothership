import redis
from threading import Thread


class OpenBotExpirySpy():
    def __init__(self):
        self.redis = redis.StrictRedis()
        self.__close_thread = True
        # for msg in pubsub.listen():
        #     print(time.time(), msg)

    def start(self):

        self.pubsub = self.redis.pubsub()
        self.pubsub.psubscribe("*")
        self.__close_thread = False
        self.__listener = Thread(target=self.listen, daemon=True)
        self.__listener.start()

    def stop(self):
        if hasattr(self, "pubsub"):
            self.pubsub.close()
        if hasattr(self, "__listener"):
            if self.__listener.is_alive():
                self.__close_thread = True

    def listen(self):
        """ Listener Thread for pubsub """
        for message in self.pubsub.listen():
            self.__callback(message)

    @property
    def callback(self):
        return self.__callback

    @callback.setter
    def callback(self, func):
        if not callable(func):
            raise TypeError("Supplied Callback is not callable.")
        else:
            self.__callback = func
