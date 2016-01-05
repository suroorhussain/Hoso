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
    original_user = user_control.User
    user_control.User, mock_user = mock.Mock(original_user), mock.Mock(original_user)

    user_control.User.return_value = mock_user
    mock_user.password = 'passwords'

    with pytest.raises(application_control.LoginError):
        user = application_control.login('username', 'password')

    user_control.User = original_user
def test_login_wronguser():
    original_path = os.path.exists
    os.path.exists = mock.Mock(original_path)
    os.path.exists.return_value = False

    with pytest.raises(application_control.LoginError):
        user = application_control.login('username', 'password')

    os.path.exists = original_path
    
def test_register():
    pass

def test_register_existing_user():
    pass

def test_select_channels():
    pass

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

