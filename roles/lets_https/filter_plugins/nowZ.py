from datetime import datetime
from time import time

def nowZ(arg):
    return datetime.utcnow().strftime('%Y%m%d%H%M%SZ')

def nowS(arg):
    return int(time())

class FilterModule(object):
    def filters(self):
        return { 'nowZ': nowZ,
                 'nowS': nowS }
