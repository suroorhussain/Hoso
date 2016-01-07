from hoso import user_control
import pickle
import __builtin__
import mock
import os.path


script_directory = os.path.dirname(user_control.__file__)

@mock.patch('__builtin__.file')
@mock.patch('pickle.dump')
def test_add_user_new(mock_dump, mock_file):
    user_control.add_user('username', 'password')

    file_path = os.path.join(script_directory, '../users/username')
    data = {'username':'username', 'password':'password', 'registered_channels':[], 'credentials':{}}
    mock_file.assert_called_with(file_path, 'wb')
    mock_dump.assert_called_with(data, file())
    
