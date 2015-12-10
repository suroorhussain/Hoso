import twitter_api
import pytest
import tweepy
import requests
requests.packages.urllib3.disable_warnings()

def test_user():
    cfg = { 
    "consumer_key"        : "HMyb0rzqSO2b4rpWw3lIONFE6",
    "consumer_secret"     : "Kt7f3ZPDsULAWbGZQ4DprdOuQCknS1eDbkmvfxclHVLVhp3wQc",
    "access_token"        : "4405674753-nnx6NeJhG7oqDptByGNAeRA6ozFCTTtQFmQLYX6",
    "access_token_secret" : "pOqpS7r7aKG2YcOsMF9dtWHbFXcvADSfo4TDaIVzBIOrY" 
    }
    
    api = twitter_api.get_api(cfg)
    assert api.me().name == 'hoso_dummy'
