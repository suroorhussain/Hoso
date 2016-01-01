import hoso.channels as channels
import mock
import tweepy
import __builtin__
import pytest

@mock.patch('__builtin__.raw_input')

def test_twitter_get_credentials(mock_raw_input):
    mock_raw_input.side_effect = ['consumer_key', 'consumer_secret', 'access_token', 'access_token_secret']
    
    t = channels.Twitter()
    credentials = t.get_credentials()

    assert credentials == { 'consumer_secret' : 'consumer_secret', 
                            'access_token' : 'access_token', 
                            'consumer_key' : 'consumer_key', 
                            'access_token_secret' : 'access_token_secret'}


def test_auth_correct():
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

    t = channels.Twitter()

    api = t.authenticate({'consumer_secret' :"test_consumer_secret",
                          'access_token' :"test_access_token",
                          'consumer_key':"test_consumer_key",
                          'access_token_secret' :"test_access_token_secret"})
    mock_OAuthHandler.assert_called_with("test_consumer_key", "test_consumer_secret")
    mock_auth.set_access_token.assert_called_with("test_access_token","test_access_token_secret")
    mock_API.assert_called_with(mock_auth)
    assert t.consumer_key == 'test_consumer_key'
    assert t.consumer_secret == 'test_consumer_secret'
    assert t.access_token == 'test_access_token'
    assert t.access_token_secret == 'test_access_token_secret'

    tweepy.OAuthHandler = original_OAuthHandler
    tweepy.API = original_API

def test_auth_fail():
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
    mock_api.me.side_effect = tweepy.TweepError({'Error message':'error code'})


    t = channels.Twitter()
    with pytest.raises(channels.ChannelError):
        t.authenticate({'consumer_secret' :"test_consumer_secret",
                        'access_token' :"test_access_token",
                        'consumer_key':"test_consumer_key",
                        'access_token_secret' :"test_access_token_secret"})
    tweepy.OAuthHandler = original_OAuthHandler
    tweepy.API = original_API

   
def test_broadcast_success():
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

    t = channels.Twitter()
    t.authenticate({'consumer_secret' :"test_consumer_secret",
                    'access_token' :"test_access_token",
                    'consumer_key':"test_consumer_key",
                    'access_token_secret' :"test_access_token_secret"})
    t.broadcast('msg')
    mock_api.update_status.assert_called_with(status="msg")
    
    tweepy.OAuthHandler = original_OAuthHandler
    tweepy.API = original_API

def test_broadcast_fail():
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
   
    mock_api.update_status.side_effect = tweepy.TweepError({'Error message':'error code'})

    t = channels.Twitter()
    with pytest.raises(channels.ChannelError):
        t.authenticate({'consumer_secret' :"test_consumer_secret",
                        'access_token' :"test_access_token",
                        'consumer_key':"test_consumer_key",
                        'access_token_secret' :"test_access_token_secret"})
        t.broadcast('msg')
    
    tweepy.OAuthHandler = original_OAuthHandler
    tweepy.API = original_API
