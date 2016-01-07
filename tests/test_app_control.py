from hoso import application_control
from hoso import user_control
import pytest
import mock
import os.path

def test_login():
    original_user = user_control.User
    user_control.User, mock_user = mock.Mock(original_user), mock.Mock(original_user)
    original_path = os.path.exists
    os.path.exists = mock.Mock(original_path)
    os.path.exists.return_value = True
    user_control.User.return_value = mock_user
    mock_user.password = 'password'

    user = application_control.login('username', 'password')

    user_control.User.assert_called_with('username')
    assert user == mock_user

    user_control.User = original_user
    os.path.exists = original_path
    
def test_login_wrongpass():
    original_path = os.path.exists
    os.path.exists = mock.Mock(original_path)
    os.path.exists.return_value = True
    original_user = user_control.User
    user_control.User, mock_user = mock.Mock(original_user), mock.Mock(original_user)

    user_control.User.return_value = mock_user
    mock_user.password = 'passwords'

    with pytest.raises(application_control.LoginError):
        user = application_control.login('username', 'password')

    user_control.User = original_user
    os.path.exists = original_path
    
def test_login_wronguser():
    original_path = os.path.exists
    os.path.exists = mock.Mock(original_path)
    os.path.exists.return_value = False

    with pytest.raises(application_control.LoginError):
        user = application_control.login('username', 'password')

    os.path.exists = original_path

def test_register():
    original_user = user_control.User
    user_control.User, mocked_user_ob = mock.Mock(), mock.Mock()
    user_control.User.return_value = mocked_user_ob

    original_path = os.path.exists
    os.path.exists = mock.Mock(original_path)
    os.path.exists.return_value = False

    ob = application_control.register('username', 'password')
    user_control.User.assert_called_with('username')
    
    mocked_user_ob.add_user.assert_called_with('username','password')
    assert ob == mocked_user_ob
    
    user_control.User = original_user
    os.path.exists = original_path

def test_register_existing_user():
    original_path = os.path.exists
    os.path.exists = mock.Mock(original_path)
    os.path.exists.return_value = True
    with pytest.raises(application_control.userNameError):
        application_control.register('username', 'password')
    os.path.exists = original_path

def test_select_channels_1():
    #Test to add channel to users registered channels if channel does not exist in users registered channels 

    original_user = user_control.User
    user_control.User = mock.Mock()
    mocked_ob = user_control.User
    channel_list = ['mail']
    mocked_ob.registered_channels = ['Twitter']
    application_control.select_channels(channel_list, mocked_ob)
    mocked_ob.add_channel.assert_called_with('mail')
    assert application_control.selected_channels == channel_list
    user_control.User = original_user

def test_select_channels_2():
    #Test to avoid adding to users registered channels if channel already exist in users registered channels 

    original_user = user_control.User
    user_control.User = mock.Mock()
    mocked_ob = user_control.User
    channel_list = ['Twitter']
    mocked_ob.registered_channels = ['Twitter']
    application_control.select_channels(channel_list, mocked_ob)
    mocked_ob.add_channel.assert_not_called()
    assert application_control.selected_channels == channel_list
    user_control.User = original_user

def test_view_selected_channels():
    application_control.selected_channels = ['Twitter','Facebook']
    view_channels = application_control.view_selected_channels()
    assert application_control.selected_channels == view_channels

def test_deselect():
    selected_channels = ['Twitter', 'Facebook', 'Mail']
    application_control.selected_channels = ['Twitter', 'Facebook', 'Mail']
    application_control.deselect('Mail')
    selected_channels.remove('Mail')
    assert application_control.selected_channels == selected_channels

def test_deselect_notesxisting():
    application_control.selected_channels = []
    with pytest.raises(application_control.Channel_name_Error):
        application_control.deselect('FaceBook')

def test_logout():
    user = mock.Mock(user_control.User) 
    
    application_control.logout(user)

    user.save_user_data.assert_called_with()
