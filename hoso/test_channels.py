import channels
import random
#from mock import Mock
import tweepy
from channels import twitter

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

