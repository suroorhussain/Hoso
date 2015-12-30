import facebook
import tweepy
import sendgrid
from sendgrid import SendGridError, SendGridClientError, SendGridServerError
import os


class channel(object): #Abstract class for all channels
        
    def authentication(self):
        raise NotImplementedError

    def broadcast(self):
        raise NotImplementedError

    def get_credentials(self):
        raise NotImplementedError
                
class Twitter(channel): #Class for twitter
    ''' This class makes use of twitter api tweepy and it is reponsible for authenticating the user and posting the tweet'''
    def get_credentials(self):
        consumer_key = raw_input("Enter consumer key > ")
        consumer_secret = raw_input("Enter consumer secret > ")
        access_token = raw_input("Enter access token > ")
        access_token_secret = raw_input("Enter access token secret >")
        twitter_credentials = { 'consumer_key' : consumer_key, 'consumer_secret' : consumer_secret, 'access_token' : access_token, 'access_token_secret' : access_token_secret }
        return twitter_credentials

    
    def authenticate(self, twitter_credentials):

        auth = tweepy.OAuthHandler(twitter_credentials['consumer_key'], twitter_credentials['consumer_secret'])
        auth.set_access_token(twitter_credentials['access_token'], twitter_credentials['access_token_secret'])
        api = tweepy.API(auth)
        try: 
            user = api.me()
        except tweepy.TweepError as e:
            message = "e[0][0]['message']"
            code = "e[0][0]['code']"
            raise ChannelError(message, code)
        
        self.consumer_key = twitter_credentials['consumer_key']
        self.consumer_secret = twitter_credentials['consumer_secret']
        self.access_token = twitter_credentials['access_token']
        self.access_token_secret = twitter_credentials['access_token_secret']

        
    
    def broadcast(self, message):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        try:
            api.update_status(status=message)
        except tweepy.TweepError as e:
            message = "e[0][0]['message']"
            code = "e[0][0]['code']"
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

        
class Facebook(channel):
            
    def authenticate(self, credentials):
        try:
            user = facebook.GraphAPI(credentials['access_token']).get_object("me")
        except facebook.GraphAPIError as e:
            raise ChannelError(e[0], -1)
        self.access_token = credentials['access_token']

    def broadcast(self, status):
        graph = facebook.GraphAPI(self.access_token)
        try:
            graph.put_object("me", "feed", message = status)
        except facebook.GraphAPIError as e:
            raise ChannelError(e[0], -1)
    
class ChannelError(Exception):
    
    def __init__(self, message, code):
        self.message = message
        self.code = code
        Exception.__init__(self, self.message)
