from hoso import application_control
import mock
from hoso import user_control
import pytest
import os.path

def test_login():
    pass

def test_login_wronguser():
    pass

def test_login_wrongpass():
    pass

def test_register():
    pass

def test_register_existing_user():
    username = 'test_usr'
    password = 'password'
    path = os.path.exists(username)
    with pytest.raises(application_control.userNameError):
        application_control.register(username, password)


def test_get_all_channels():
    pass

def test_select_channels():
    channel_list = ['Twitter', 'Facebook']
    selected_channels = []
    user_ob = user_control.User('test_user')
    original_add_channel = user_ob.add_channel
    mocked_add_channel = mock.Mock()
    user_ob.add_channel = mocked_add_channel
    registered_channels = ['Facebook']

    for i in range(len(channel_list)):
        if channel_list[i] not in user_ob.registered_channels:
            mocked_add_channel.assert_called_with(channel_list(i))
    application_control.select_channels(channel_list, user_ob)
    assert application_control.selected_channels == channel_list
    user_ob.add_channel = original_add_channel

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

