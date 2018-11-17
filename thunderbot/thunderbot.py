from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import listen_to
import re

class ThunderBotPlugin(MachineBasePlugin):

    @listen_to(regex=r'^#(?P<colour>([0-9a-fA-F]{2}){3}|([0-9a-fA-F]){3})$')
    def thunder(self, msg, colour=None):
        print("Thunder #{}".format(colour))



