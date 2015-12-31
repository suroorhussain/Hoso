import hoso.user_control
import pickle

with open("../users/test_user", 'rb') as handle:
    original_data = pickle.loads(handle.read())

test_user = user_control.User('test_user')

def test_my_channels():
    pass

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


with open("../users/test_user", 'rb') as handle:
    pickle.dump(original_data, handle)
