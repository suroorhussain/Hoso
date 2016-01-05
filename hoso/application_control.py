from hoso import user_control
import os.path

selected_channels = []
curdir = getdir(__file__)

def login(username, password):
    if os.path.exists(os.path.join(curdir, '../users/'+username)):
        user = user_control.User(username)
        if user.password == password:
            return user
    
def register(username, password):
    pass

def get_all_channels():
    with open(os.path.join(curdir, "channel_list.txt"), 'r') as channel_list:
        return channel_list.readlines()

def select_channels(channel_list, ob):
    pass

def view_selected_channels():
    return selected_channels

def deselect(channel_name):
    if channel_name in selected_channels:
        selected_channels.remove(channel_name)
    else:
        raise Channel_name_Error('Channel does not exist')

class Channel_name_Error(Exception):
    
    def __init__(self, message):
        self.message = message
        super(Channel_name_Error, self).__init__(message)
