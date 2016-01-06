from hoso import user_control
import os.path

selected_channels = []

def login(username, password):
    pass

def register(username, password):
    if os.path.exists(username):
        raise userNameError('%s already exist'%username)
    else:
        user_control.add_user(username, password)
        user_ob = user_control.User(username)
        return user_ob

def get_all_channels():
    curdir = os.path.dirname(__file__)
    with open(os.path.join(curdir, "channel_list.txt"), 'r') as channel_list:
        return channel_list.readlines()

def select_channels(channel_list, user_ob):
    for i in range(len(channel_list)):
        if channel_list[i] not in user_ob.registered_channels:
            user_ob.add_channel(channel_list[i])
    global selected_channels
    selected_channels = channel_list

def view_selected_channels():
    return selected_channels

def deselect(channel_name):
    global selected_channels
    if channel_name in selected_channels:
        selected_channels.remove(channel_name)
    else:
        raise Channel_name_Error('Channel does not exist')

class Channel_name_Error(Exception):
    
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, self.message)

class userNameError(Exception):
    
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, self.message)
