import facebook
import sendgrid
import tweepy
import requests
request.packages.urllib3.disable_warnings()


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
    def __init__(self, consumer_key, consumer_secret, access_token,access_token_secret, message):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.message = message

    def broadcast(self, api):
        self.api = api
        try:
            status = api.update_status(status=self.message)
        except tweepy.TweepError as e:
            error_message = e[0][0]['message']
            error_code = e[0][0]['code']
            print error_message

class mail(channel): #Class for mail
    
    def __init__(self,sender,text_message):
        self.sender=To_address
        self.text_message=body
        
    def broadcast(self):
        send_message= sendgrid.sendGridclient(username,password)
        message=sendgrid.Mail()
        message.add_to("To_address")
        message.set_text("body")
        message=sendgrid.mail(to="to_address",text="body")
        status,msg= send_message.send(message)
    

   
    
