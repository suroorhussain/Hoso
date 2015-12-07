import tweepy
import message
#import urllib3

#urllib3.disable_warnings()

#from sys import argv

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "HMyb0rzqSO2b4rpWw3lIONFE6",
    "consumer_secret"     : "Kt7f3ZPDsULAWbGZQ4DprdOuQCknS1eDbkmvfxclHVLVhp3wQc",
    "access_token"        : "4405674753-nnx6NeJhG7oqDptByGNAeRA6ozFCTTtQFmQLYX6",
    "access_token_secret" : "pOqpS7r7aKG2YcOsMF9dtWHbFXcvADSfo4TDaIVzBIOrY" 
    }

  api = get_api(cfg)
  tweet = message.get_message()
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
