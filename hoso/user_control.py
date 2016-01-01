from hoso import channels
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
            self.auth_errors = ['']
            self.broadcast_errors = ['']
    def my_channels(self):
        return self.registered_channels

    def add_channel(self, channel_name):
        #if channel_name not in self.registered_channels:
            self.registered_channels.append(channel_name)
        #else:
          #  raise duplicateChannel(channel_name)
            
      #  channel = getattr(channels, channel_name)()
       # channel.get_credentials()

    def remove_channel(self, channel_name):
        self.registered_channels.remove(channel_name)

    def select_channel(self, channel_name):
        raise NotImplementedError

    def send_message(self, message):
        for media in self.selected_channels:
            channel = getattr(channels, media)()
            try:
                channel.authenticate(self.credentials[media])
            except channels.ChannelError as e:
                self.auth_errors.append(media+':'+e.message)

            try:
                channel.broadcast(message)
            except channels.ChannelError as e:
                self.broadcast_errors.append(media+':'+e.message)

        if self.auth_errors != ['']:
            auth_error = self.auth_errors
            self.auth_errors = ['']
            raise AuthenticationError(','.join(auth_error))
        elif self.broadcast_errors != ['']:
            broadcast_error = self.broadcast_errors
            self.broadcast_errors = ['']
            raise BroadcastError(','.join(broadcast_error))
            
    def save_user_data(self):
        raise NotImplementedError


def add_user(username, password):
    raise NotImplementedError

class duplicateChannel(Exception):
    
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, self.message)


class AuthenticationError(Exception):
    
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, self.message)

class BroadcastError(Exception):
    
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, self.message)
