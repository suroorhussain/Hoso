import sendgrid
import tweepy


class channel(object): #Abstract class for all channels
    def authenticate(self):
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
    

def twitter_api(cfg,message):     
    consumer_key = cfg['consumer_key']
    consumer_secret = cfg['consumer_secret']
    access_token = cfg['access_token']
    access_token_secret = cfg['access_token_secret']

    twiter=twitter(consumer_key,consumer_secret,access_token,access_token_secret, message)
    api=twiter.authentication(cfg)
    status=twiter.broadcast(api, message)
    return status
