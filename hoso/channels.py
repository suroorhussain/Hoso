import tweepy
import sendgrid
from sendgrid import SendGridError, SendGridClientError, SendGridServerError
import os


class channel(object): #Abstract class for all channels
    def authentication(self):
        raise NotImplementedError

    def broadcast(self):
        raise NotImplementedError

                
class Twitter(channel): #Class for twitter
    ''' This class makes use of twitter api tweepy and it is reponsible for authenticating the user and posting the tweet'''

    def __init__(self, consumer_key, consumer_secret, access_token,access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        return api
    
    def broadcast(self, message):
        api = self.authenticate()
        try:
            api.update_status(status=message)
        except tweepy.TweepError as e:
            message = e[0][0]['message']
            code = e[0][0]['code']
            raise ChannelError(message, code)
            

class mail(channel): #Class for mail
    
    def __init__(self,sender,text_message,consumer_key, consumer_passwd):
        self.sender = To_address
        self.text_message =body

    def authentication(self): #authentication for the mail service

        Username = os.getenv('API_USER')
        Password = os.getenv('API_KEY')
        auth = sendgrid.SendGridclient(Username, Password)
        return auth
    
    def broadcast(self , api,  message): # Broadcast message as mail 
        
        try:
            login  = sendgrid.SendGridclient(Username, Password, raise_errors =True)
        except SendGridClientError:
            error_message = 'client error'
            return error_message
        
        except SendGridServerError:
            error_message = 'ServerError'
            return error_message
    
        message = sendgrid.Mail()
        message.add_to(self.sender)
        message.set_text(self.text_message)
        try:
            message = sendgrid.mail(To = self.sender, Message = self.text_message)
            status,msg = send_message.send(message)
        except Exception:
            return "Cannot send the mail"


class ChannelError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        Exception.__init__(self, self.message)
