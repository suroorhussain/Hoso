#from twython import Twython
#twitter = Twython()

#user_timeline = twitter.getUserTimeline(screen_name='MOHAMED JASSIM')

from twython import Twython
twitter = Twython()
# First, let's grab a user's timeline. Use the
# 'screen_name' parameter with a Twitter user name.
user_timeline = twitter.getUserTimeline(screen_name="pythoncentral")
