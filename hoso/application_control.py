from hoso import user_control

selected_channels = []
user_name = 'test_user'
user_ob = user_control.User(user_name)

def login(username, password):
    pass

def register(username, password):
    pass

def get_all_channels():
    pass

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
        Exception.__init__(self, self.message)
