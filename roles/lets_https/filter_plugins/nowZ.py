from datetime import datetime

def nowZ(arg):
    return datetime.utcnow().strftime('%Y%m%d%H%M%SZ')

class FilterModule(object):
    def filters(self):
        return { 'nowZ': nowZ }
