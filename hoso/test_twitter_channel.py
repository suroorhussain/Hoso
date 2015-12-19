import mock
import tweepy
import channels

def test_auth():
    mock_OAuthHandler = mock.Mock()
    mock_auth = mock.Mock()
    mock_API = mock.Mock()
    mock_api = mock.Mock()

    original_OAuthHandler = tweepy.OAuthHandler
    original_API = tweepy.API
    tweepy.OAuthHandler = mock_OAuthHandler
    tweepy.API = mock_API

    mock_OAuthHandler.return_value = mock_auth
    mock_API.return_value = mock_api

    t = Channels.Twitter("test_consumer_key",
                "test_consumer_secret",
                "test_access_token",
                "test_access_token_secret")

    api = t.authenticate()
    mock_OAuthHandler.assert_called_with("test_consumer_key", "test_consumer_secret")
    mock_auth.set_access_token.assert_called_with("test_access_token","test_access_token_secret")
    mock_API.assert_called_with(mock_auth)

    assert api == mock_api
    
    tweepy.OAuthHandler = original_OAuthHandler
    tweepy.API = original_API
    