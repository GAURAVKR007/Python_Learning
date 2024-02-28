import tweepy
import time

auth = tweepy.OAuth1UserHandler('pnAP772zq0J3aWaLn9ipsenv5','z15qJh6BCDgOncXQSNPaq2juCPdkvwVX8M9Z2U8eYb3p2OsNas','799225511146885124-RCMul23CAA4X2b9gSjNIfdIjtDn22kT','WDom1uyM0LjCZM8p1GJmXBbo98Rg8YP1SoP67Ge3A2153')

api = tweepy.API(auth)

user = api.get_user(screen_name='@GauravKrThakur2')
# print(user.screen_name)
# print(user.name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)

def limit_handler(cursor):
   try:
      while True:
         yield cursor.next()
   except tweepy.TooManyRequests:
      time.sleep(300)
   except StopIteration:
      return

# Generous Bot
# for follower in limit_handler(tweepy.Cursor(api.get_followers,screen_name='@GauravKrThakur2').pages(1)):
#    for i in range(len(follower)):
#       print(follower[i].name)
#       if follower[i].name == 'Prokira':
#          follower[i].unfollow()
#          break

search_string = 'GTR'
numberOfTweets = 20

for tweet in limit_handler(tweepy.Cursor(api.search_tweets,search_string).items(numberOfTweets)):
   try:
      tweet.favorite()
      print('I liked that tweet')
   except AttributeError as e:
      print(e.reason)
   except StopIteration:
      break
