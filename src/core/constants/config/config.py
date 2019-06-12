import yaml
import os
class Config(object):
    @property
    def core(self):
        """ Get Core Config """
        with open("config/runtime/core.yaml") as core:
            parsed = yaml.safe_load(core)
        return parsed

