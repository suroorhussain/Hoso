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
           
        
