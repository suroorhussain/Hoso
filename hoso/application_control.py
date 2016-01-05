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
