class channel(object): #Abstract class for all channels
    def authenticate(self):
        raise NotImplementedError

    def broadcast(self):
        raise NotImplementedError


class facebook(channel): #Class for facebook
    pass

class twitter(channel): #Class for twitter
    pass

class mail(channel): #Class for mail
    pass
