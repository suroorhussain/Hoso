from google.appengine.api import mail
import facebook


class channel(object): #Abstract class for all channels
    def authenticate(self):
        raise NotImplementedError

    def broadcast(self):
        raise NotImplementedError


class fb(channel): #Class for facebook
    def __init__(self, token, message):
        self.access_token = token
        self.post = message
        
    def broadcast(self):
        graph = facebook.GraphAPI(self.access_token)
        return graph.put_object("me", "feed", message = self.post)
class twitter(channel): #Class for twitter
    pass

class mail(channel): #Class for mail
    message=mail.EmailMessage(sender="username",subject="subject")
    message.to="To"
    message.body="subject"
    message.sent()
    pass
