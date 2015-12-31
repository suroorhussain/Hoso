from hoso import user_control
import pickle
import os .path

curdir = os.path.dirname(__file__)
with open(os.path.join(curdir, "../users/test_user"), 'rb') as handle:
    original_data = pickle.loads(handle.read())

test_user = user_control.User('test_user')

def test_my_channels():
    channels_list = test_user.my_channels()
    channels_in_file = original_data['registered_channels']
    assert channels_list == channels_in_file

def test_add_channel():
    pass

def test_remove_channel():
    pass

def test_select_channel():
    pass

def test_send_message():
    pass

def test_logout():
    pass


with open(os.path.join(curdir, "../users/test_user"), 'wb') as handle:
    pickle.dump(original_data, handle)
