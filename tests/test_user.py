from hoso import user_control
import pickle
import os .path
from hoso import channels
import mock
import pytest
<<<<<<< HEAD
=======

>>>>>>> 35dfa7e0b5c4999147bf19bc114bf8990fc02a16

curdir = os.path.dirname(__file__)
with open(os.path.join(curdir, "../users/test_user"), 'rb') as handle:
    original_data = pickle.loads(handle.read())

user_data = original_data
test_user = user_control.User('test_user')

def test_my_channels():
    channels_list = test_user.my_channels()
    channels_in_file = original_data['registered_channels']
    assert channels_list == channels_in_file


def test_add_channel_name():
    test_user.remove_channel('Twitter')
    test_user.add_channel('Twitter')
    original_data['registered_channels'].remove('Twitter')
    original_data['registered_channels'].append('Twitter')
    assert original_data['registered_channels'] == test_user.registered_channels

def test_add_channel_credentials():
    original_twitter = channels.Twitter
    original_facebook = channels.Facebook
    channels.Twitter, mocked_twitter = mock.Mock(original_twitter), mock.Mock(original_twitter)
    channels.Facebook, mocked_facebook = mock.Mock(original_facebook), mock.Mock(original_facebook)

    channels.Facebook.return_value = mocked_facebook
    channels.Twitter.return_value = mocked_twitter
    mock_fb_credentials = mock.Mock()
    mock_twitter_credentials = mock.Mock()

    mocked_facebook.get_credentials.return_value = mock_fb_credentials
    mock_fb_credentials = {'access_token':'token'}
    test_user.add_channel_credentials('Facebook')
    
    mocked_twitter.get_credentials.return_value = mock_twitter_credentials
    mock_twitter_credentials = {'access_token' : 'token',
                                'access_token_secret' : 'token_secret',
                                'consumer_key': 'key',
                                'consumer_secret' : 'secret'}
    test_user.add_channel_credentials('Facebook')
    
    assert test_user.credentials['Twitter'] == mock_twitter_credentials
    assert test_user.credentials['Facebook'] == mock_fb_credentials

    channels.Twitter = original_twitter
    channels.Facebook = original_facebook

def test_add_duplicate_channel():
    with pytest.raises(user_control.DuplicateChannel):
        test_user.add_channel('Twitter')
    
def test_remove_channel_name():
    original_data['registered_channels'].remove('Facebook')
    test_user.remove_channel('Facebook')
    assert test_user.registered_channels == original_data['registered_channels']
'''
def test_remove_channel_credentials():
    credentials = original_data['credentials']
    del credentials['Twitter']
    test_user.remove_channel_credentials('Twitter')
    assert credentials == test_user.credentials
    test_user.add_channel('Twitter')
    test_user.credentials = original_data['credentials']
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
    
    selected_channels = ['Twitter', 'Facebook']
    test_user.send_message('message', selected_channels)

    mocked_twitter.authenticate.assert_called_with(test_user.credentials['Twitter'])
    mocked_twitter.broadcast.assert_called_with('message')

    mocked_facebook.authenticate.assert_called_with(test_user.credentials['Facebook'])
    mocked_facebook.broadcast.assert_called_with('message')

    channels.Twitter = original_twitter
    channels.Facebook = original_facebook
    
def test_send_message_auth_fail():
    original_twitter = channels.Twitter
    original_facebook = channels.Facebook
    channels.Twitter, mocked_twitter = mock.Mock(original_twitter), mock.Mock(original_twitter)
    channels.Facebook, mocked_facebook = mock.Mock(original_facebook), mock.Mock(original_facebook)

    channels.Facebook.return_value = mocked_facebook
    channels.Twitter.return_value = mocked_twitter
    mocked_facebook.authenticate.side_effect = channels.ChannelError('authentication error', -1)
    mocked_twitter.authenticate.side_effect = channels.ChannelError('authentication error', -1)

    selected_channels = ['Twitter', 'Facebook']
    with pytest.raises(user_control.AuthenticationError):
        test_user.send_message('message', selected_channels)

    channels.Twitter = original_twitter
    channels.Facebook = original_facebook

def test_send_message_broadcast_fail():
    original_twitter = channels.Twitter
    original_facebook = channels.Facebook
    channels.Twitter, mocked_twitter = mock.Mock(original_twitter), mock.Mock(original_twitter)
    channels.Facebook, mocked_facebook = mock.Mock(original_facebook), mock.Mock(original_facebook)

    channels.Facebook.return_value = mocked_facebook
    channels.Twitter.return_value = mocked_twitter
    mocked_facebook.broadcast.side_effect = channels.ChannelError('authentication error', -1)
    mocked_twitter.broadcast.side_effect = channels.ChannelError('authentication error', -1)

    selected_channels = ['Twitter', 'Facebook']
    with pytest.raises(user_control.BroadcastError):
        test_user.send_message('message', selected_channels)

    channels.Twitter = original_twitter
    channels.Facebook = original_facebook
def test_save_user_data():
    test_data = {
        'username':test_user.username,
        'password':test_user.password,
        'registered_channels':test_user.registered_channels,
        'credentials':test_user.credentials
        }
    test_user.save_user_data()

    with open(os.path.join(curdir, "../users/test_user"), 'rb') as handle:
         data = pickle.loads(handle.read())
    assert test_data == data


<<<<<<< HEAD
#with open(os.path.join(curdir, "../users/test_user"), 'wb') as handle:
 #   pickle.dump(original_data, handle)
=======
with open(os.path.join(curdir, "../users/test_user"), 'wb') as handle:
    pickle.dump(original_data, handle)
print original_data
>>>>>>> 35dfa7e0b5c4999147bf19bc114bf8990fc02a16
