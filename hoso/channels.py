import tweepy
import sendgrid
from sendgrid import SendGridError, SendGridClientError, SendGridServerError
import os


class channel(object): #Abstract class for all channels
    def authentication(self):
        raise NotImplementedError

    def broadcast(self):
        raise NotImplementedError

                
class twitter(channel): #Class for twitter

    def __init__(self, consumer_key, consumer_secret, access_token,access_token_secret, message):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.message = message
        
    def authentication(self,cfg):
        auth = tweepy.OAuthHandler(self.consumer_key,self.consumer_secret)
        auth.set_access_token(self.access_token,self.access_token_secret)
        api = tweepy.API(auth)
        user_name = api.me().name
        return api
 
    def broadcast(self, api, message):
        error_message =''
        try:
            status = api.update_status(status=self.message)
            return error_message
        except tweepy.TweepError as e:
            error_message = e[0][0]['message']
            error_code = e[0][0]['code']
            #print error_message
            return error_message


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
            error_message = 'client errror'
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
           
        
def twitter_api(cfg,message):     
    consumer_key = cfg['consumer_key']
    consumer_secret = cfg['consumer_secret']
    access_token = cfg['access_token']
    access_token_secret = cfg['access_token_secret']

    twiter=twitter(consumer_key,consumer_secret,access_token,access_token_secret, message)
    api=twiter.authentication(cfg)
    status=twiter.broadcast(api, message)
    return status
