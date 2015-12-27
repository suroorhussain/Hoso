import hoso.channels as channels
import mock
import tweepy
import __builtin__

def test_raw_input(monkeypatch):
    def mock_raw_input():
         mock_consumer_key = mock.Mock()
         mock_consumer_secret = mock.Mock()
         mock_access_token = mock.Mock()
         mock_access_token_secret = mock.Mock()

         mock_consumer_key.return_value = 'key1'
         mock_consumer_secret.return_value = 'key2'
         mock_access_token.return_value = 'key3'
         mock_access_token_secret.return_value = 'key4'

         mock_dict = mock.Mock()
         mock_dict.return_value = {'consumer_key': mock_consumer_key.return_value, 'consumer_secret' : mock_consumer_secret.return_value, 'access_token' : mock_access_token.return_value, 'access_token_secret' : mock_access_token_secret.return_value}
         return mock_dict.return_value
    
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    retval = raw_input()
    
    assert retval == {'consumer_key' : 'key1', 'consumer_secret':'key2', 'access_token' : 'key3', 'access_token_secret' : 'key4'}
    
    

'''
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

    t = channels.Twitter("test_consumer_key",
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
    
def test_broadcast():
    mock_api = mock.Mock()
    t = channels.Twitter("test_consumer_key", 
                "test_consumer_secret", 
                "test_access_token",
                "test_access_token_secret")
    t.authenticate = mock.Mock()
    t.authenticate.return_value = mock_api
    t.broadcast('msg')
    mock_api.update_status.assert_called_with(status="msg")
    
'''
