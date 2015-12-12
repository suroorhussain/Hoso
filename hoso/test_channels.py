import channels
import random
#import facebook
#from mock import Mock
import tweepy

from channels import twitter


#access_token = """CAACEdEose0cBABzZAIKQQ4DTrbJS0sru0heXJwIm70abeOF705azqlgx9ulWi9GCHorQcFDIptDWSR1CVnb6hBDlDk1ZAUa1P4YPTAplTvPWzIPxAZAymEEtnjQGcYOG2KdZClZBaardPGKC153upC7w4C4KY5O3KgsqOj01CO4yrEV99rUBhMmjtrkZB8fEuYzsMa8idJ6gZDZD"""
#message = "Duplication test"
#def test_facebook_broadcast():
  #  graph = facebook.GraphAPI(access_token)
    #user = graph.get_object("me")
   # face_book = channels.fb(access_token, message)
  #  result = face_book.broadcast()
 #   assert user["id"] in result["id"]

#def test_facebook_broadcast_expiry():
#    access_token = """CAACEdEose0cBADHPW80j9CVomN5gjM1ssVmA6oqPm0UVUvAtOUBWz9mxfSYElFvhH5VFmS6osdYCWUYxTB9yNSdaG9E8q6VlGZA6LZAPAIccdqsbiCglJ5V7mZBWP0hXBGGg5WjDiltuZB8OCB4qs5DFWFzVsB2W3cWVCwwXfeq7OcLLDZCaYFbmINRhYXU4b7hGYBkdFAwZDZD"""
   # graph = facebook.GraphAPI(access_token)
   # try:
  #      user = graph.get_object("me")
 #   except facebook.GraphAPIError as e:
#        assert 'expired' in e[0]

#def test_facebook_broadcast_duplicate_message():
   # graph = facebook.GraphAPI(access_token)
  #  user = graph.get_object("me")
 #   face_book = channels.fb(access_token, message)
   # try:
  #      face_book.broadcast()
 #   except facebook.GraphAPIError as e:
#        assert e[0] == 'Duplicate status message'

def test_twitter_athentication_correct():
    cfg = { 
        "consumer_key"        : "HMyb0rzqSO2b4rpWw3lIONFE6",
        "consumer_secret"     : "Kt7f3ZPDsULAWbGZQ4DprdOuQCknS1eDbkmvfxclHVLVhp3wQc",
        "access_token"        : "4405674753-nnx6NeJhG7oqDptByGNAeRA6ozFCTTtQFmQLYX6",
        "access_token_secret" : "pOqpS7r7aKG2YcOsMF9dtWHbFXcvADSfo4TDaIVzBIOrY" 
    }
    message = 'working on hoosoo'+str(random.random())
    status = channels.twitter_api(cfg, message)
    assert status == ''

def test_twitter_athentication_wrong():
    cfg = { 
        "consumer_key"        : "b0rzqSO2b4rpWw3lIONFE6",
        "consumer_secret"     : "Kt7f3ZPDsULAWbGZQ4DprdOuQCknS1eDbkmvfxclHVLVhp3wQc",
        "access_token"        : "5674753-nnx6NeJhG7oqDptByGNAeRA6ozFCTTtQFmQLYX6",
        "access_token_secret" : "qpS7r7aKG2YcOsMF9dtWHbFXcvADSfo4TDaIVzBIOrY" 
    }
    message = 'working on '
    try:
        status = channels.twitter_api(cfg, message)
    except tweepy.TweepError as e:
        error_message = e[0][0]['message']
        assert error_message == 'Invalid or expired token.'

#def test_mail_broadcast():
 #   mock=Mock()
  #  mock.add_to()
   # mock.attribute="send_to _address"
    #mock.add_to.assert_called_with()
 #   mock.set_text()
  #  mock.attribute="text_message"
   # mock.set_text.assert_called_with()
