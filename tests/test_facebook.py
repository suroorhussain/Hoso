import facebook
import hoso.channels as facebook_api
import mock
import pytest
import __builtin__


def test_facebook_authenticate():
    original_graph = facebook.GraphAPI
    facebook.GraphAPI = mock.Mock(original_graph)
    mock_graph = mock.Mock(original_graph)
    facebook.GraphAPI.return_value = mock_graph
    
    fb = facebook_api.Facebook()
    fb.authenticate("token")

    facebook.GraphAPI.assert_called_with("token")
    mock_graph.get_object.assert_called_with("me")
    assert fb.auth_status

    facebook.GraphAPI = original_graph

def test_facebook_authenticate_fail():
    original_graph = facebook.GraphAPI
    facebook.GraphAPI = mock.Mock(original_graph)
    mock_graph = mock.Mock(original_graph)
    facebook.GraphAPI.return_value = mock_graph
    mock_graph.get_object.side_effect = facebook.GraphAPIError({'Error_description':'Token expired'})

    fb = facebook_api.Facebook()
    with pytest.raises(facebook_api.ChannelError):
        fb.authenticate("token")

    facebook.GraphAPI = original_graph
        
    
def test_facebook_broadcast_success():
    original_graph = facebook.GraphAPI
    facebook.GraphAPI = mock.Mock(original_graph)
    graph_mock = mock.Mock(original_graph)
    facebook.GraphAPI.return_value = graph_mock
    
    fb = facebook_api.Facebook()
    fb.authenticate("token")
    fb.broadcast("my post")

    facebook.GraphAPI.assert_called_with("token")
    graph_mock.put_object.assert_called_with("me", "feed", message = "my post")

    facebook.GraphAPI = original_graph

def test_facebook_broadcast_error():
    original_graph = facebook.GraphAPI
    facebook.GraphAPI = mock.Mock(original_graph)
    graph_mock = mock.Mock(original_graph)
    facebook.GraphAPI.return_value = graph_mock
    graph_mock.put_object.side_effect = facebook.GraphAPIError({"error_description":"Error while broadcasting"})

    fb = facebook_api.Facebook()
    fb.authenticate("token")
    with pytest.raises(facebook_api.ChannelError):
        fb.broadcast("my post")
        
    facebook.GraphAPI = original_graph
    
@mock.patch('__builtin__.raw_input')
def test_facebook_get_credentials(mock_raw_input):
    mock_raw_input.return_value = 'token'

    fb = facebook_api.Facebook()
    cred = fb.get_credentials()
    
    mock_raw_input.assert_called_with("Please enter the access token obtained from https://developers.facebook.com/tools/explorer: ")
    assert cred == {'access_token':'token'}
    
    

