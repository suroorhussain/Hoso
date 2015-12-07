class channel(object):
    def authenticate(self):
        raise NotImplementedError

    def broadcast(self):
        raise NotImplementedError


class facebook(channel):
    pass

class twitter(channel):
    pass

class mail(channel):
    pass
