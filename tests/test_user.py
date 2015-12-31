from hoso import user_control
import pickle
import os .path
from hoso import channels
import mock

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
'''
def test_remove_channel():
    channels_of_user = original_data['registered_channels']
    credentials = original_data['credentials']
    channel_to_remove = 'Twitter'
    channels_of_user.remove('Twitter')
    del credentials['Twitter']
    test_user.remove_channel('Twitter')
    assert channels_of_user == test_user.registered_channels
    assert credentials == test_user.credentials
    test_user.credentials = original_data['credentials']
    test_user.registered_channels = original_data['registered_channels']
'''    

def test_select_channel():
    pass

def test_send_message():
    original_twitter = channels.Twitter
    original_facebook = channels.Facebook
    channels.Twitter, mocked_twitter = mock.Mock(original_twitter), mock.Mock(original_twitter)
    channels.Facebook, mocked_facebook = mock.Mock(original_facebook), mock.Mock(original_facebook)

    channels.Facebook.return_value = mocked_facebook
    channels.Twitter.return_value = mocked_twitter
    
    test_user.selected_channels = ['Twitter', 'Facebook']
    test_user.send_message('message')

    mocked_twitter.authenticate.assert_called_with(test_user.credentials['Twitter'])
    mocked_twitter.broadcast.assert_called_with('message')

    mocked_facebook.authenticate.assert_called_with(test_user.credentials['Facebook'])
    mocked_facebook.broadcast.assert_called_with('message')

    channels.Twitter = original_twitter
    channels.Facebook = original_facebook

def test_save_user_data():
    pass


with open(os.path.join(curdir, "../users/test_user"), 'wb') as handle:
    pickle.dump(original_data, handle)
