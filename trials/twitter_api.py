import tweepy
import message
import requests
requests.packages.urllib3.disable_warnings()

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def get_tweet():
  return message.get_message()

def return_code(error_code):
  return error_code

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "HMyb0rzqSO2b4rpWw3lIONFE6",
    "consumer_secret"     : "Kt7f3ZPDsULAWbGZQ4DprdOuQCknS1eDbkmvfxclHVLVhp3wQc",
    "access_token"        : "4405674753-nnx6NeJhG7oqDptByGNAeRA6ozFCTTtQFmQLYX6",
    "access_token_secret" : "pOqpS7r7aKG2YcOsMF9dtWHbFXcvADSfo4TDaIVzBIOrY" 
    }
  error_code = 0
  api = get_api(cfg)
  tweet = get_tweet()
  user_name = api.me().name 
  print "user --> {}".format(user_name)
  try: 
    status = api.update_status(status=tweet) 
  except tweepy.TweepError as e:
    message = e[0][0]['message']
    error_code = e[0][0]['code']
  print "error code: {}".format(error_code)
  print message
  return_code(error_code)

  
# Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
