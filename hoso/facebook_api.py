import facebook


class channel(object): #Abstract class for all channels
    def authenticate(self):
        raise NotImplementedError

    def broadcast(self):
        raise NotImplementedError

    
class ChannelError(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code

        Exception.__init__(self, self.message)

        
class Facebook(channel):

    def __init__(self, token = None):
        if not token == None:
            self.access_token = token

    def broadcast(self, status):
        graph = facebook.GraphAPI(self.access_token)
        try:
            graph.put_object("me", "feed", message = status)
        except facebook.GraphAPIError as e:
            raise ChannelError(e[0], -1)

