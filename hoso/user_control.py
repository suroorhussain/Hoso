import hoso.channels
import pickle
import os.path

class User(object):

    def __init__(self, username):
        current_directory = os.path.dirname(__file__)
        with open(os.path.join(current_directory, '../users/'+ username), 'rb') as user_file:
            user_data = pickle.loads(user_file.read())
            self.password = user_data['password']
            self.registered_channels = user_data['registered_channels']
            self.credentials = user_data['credentials']
            
    def my_channels(self):
        return self.registered_channels

    def add_channel(self, channel_name):
        raise NotImplementedError

    def remove_channel(self, channel_name):
        raise NotImplementedError

    def select_channel(self, channel_name):
        raise NotImplementedError

    def send_message(self, message):
         for media in self.selected_channels:
            channel = getattr(hoso.channels, media)()
            channel.authenticate(self.credentials[media])
            channel.broadcast(message)
            
    def save_user_data(self):
        raise NotImplementedError


def add_user(username, password):
    raise NotImplementedError


class AuthenticationError(Exception):
    
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, self.message)


class BroadcastError(Exception):
    
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, self.message)
