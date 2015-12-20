import facebook
import facebook_api
import status_generator
import mock
import pytest


def test_facebook_broadcast_success():
    original_graph = facebook.GraphAPI
    facebook.GraphAPI = mock.Mock(original_graph)
    graph_mock = mock.Mock(original_graph)
    facebook.GraphAPI.return_value = graph_mock
    
    fb = facebook_api.Facebook("token")
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

    fb = facebook_api.Facebook("token")
    with pytest.raises(facebook_api.ChannelError):
        fb.broadcast("my post")
        
    facebook.GraphAPI = original_graph

