import channels
import pickle
import os.path

class User(object):

    def __init__(self, username):
        current_directory = os.path.dirname(__file__)
        with open(os.path.join(current_directory, '../users/'+ username), 'rb') as user_file:
            user_data = pickle.loads(user_file.read())
            self.username = username
            self.password = user_data['password']
            self.registered_channels = user_data['registered_channels']
            self.credentials = user_data['credentials']
            self.auth_errors = []
            self.broadcast_errors = []
    def my_channels(self):
        return self.registered_channels

    def add_channel(self, channel_name):
        if channel_name in self.registered_channels:
            raise DuplicateChannel('Error because channel already exist')
        else:
            self.registered_channels.append(channel_name)
            channel = getattr(channels, channel_name)()
            channel_credentials = channel.get_credentials()
            self.credentials[channel_name] = channel_credentials
        
    def remove_channel(self, channel_name):
        self.registered_channels.remove(channel_name)
        del self.credentials[channel_name]

    def send_message(self, message, selected_channels):
        for media in selected_channels:
            channel = getattr(channels, media)()
            try:
                channel.authenticate(self.credentials[media])
            except channels.ChannelError as e:
                self.auth_errors.append(media+':'+e.message)
                continue

            try:
                channel.broadcast(message)
            except channels.ChannelError as e:
                self.broadcast_errors.append(media+':'+e.message)
                continue
            
        if self.auth_errors != [] or self.broadcast_errors != []:
            auth_error = self.auth_errors
            broadcast_error = self.broadcast_errors
            self.auth_errors = []
            self.broadcast_errors = []
            error_message = 'Authentication Errors: '+','.join(auth_error)+'\n Broadcast Error: '+','.join(broadcast_error)
            raise UserError(error_message)
        
    def save_user_data(self):
         user_data = {
        'username':self.username,
        'password':self.password,
        'registered_channels':self.registered_channels,
        'credentials':self.credentials
        }
         current_directory = os.path.dirname(__file__)
         with open(os.path.join(current_directory, '../users/'+ self.username), 'wb') as user_file:
             pickle.dump(user_data, user_file)


def add_user(username, password):
     data = {'username':username, 'password':password, 'registered_channels':[], 'credentials':{}}
     current_directory = os.path.dirname(__file__)
     filename = file(os.path.join(current_directory, '../users/'+ username), 'wb')
     pickle.dump(data, filename)
     filename.close()

class DuplicateChannel(Exception):
    
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, self.message)
   
class UserError(Exception):
    
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, self.message)
