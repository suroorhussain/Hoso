import facebook
import sendgrid


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
    def broadcast(self):
        send_message= sendgrid.sendGridclient(username,password)
        message=sendgrid.Mail()
        message.add_to("To_address")
        message.set_text("body")
        message=sendgrid.mail(to="to_address",text="body")
        status,msg= send_message.send(message)
    

   
    pass
