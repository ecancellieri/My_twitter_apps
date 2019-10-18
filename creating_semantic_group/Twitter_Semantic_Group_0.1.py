#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tweepy import OAuthHandler
import tweepy
import csv
import pandas as pd
import re


# In[2]:


# Twitter user application details needed to connect to the Twitter API.
consumer_key = "XXX"
consumer_secret = "YYY"
access_token = "WWW"
access_token_secret = "ZZZ"


# In[3]:


# Set up the API connection and test authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# In[4]:


# Creates the user object. The me() method returns the user whose authentication keys were used.
user = api.me()
 
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))


# In[5]:


def text_clean(inputString):
    out_string = inputString.encode('ascii', 'ignore').decode('ascii')
    out_string = re.sub(r"http\S+"  , '', out_string.lower())
    out_string = re.sub('@[^\s]+'   , '', out_string.lower())
    out_string = re.sub('[!?,.:";-]', '', out_string)
    out_string = re.sub('\d+'       , '', out_string)
    out_string = re.sub('\n'        , '', out_string)
    return out_string

def download_days(word,day1,day2):
    # Open/Create a file to append data
    csvFile = open(word + '.csv', 'a', newline='')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['tweet.created_at', 'tweet.id', 'tweet.user.screen_name', 'tweet.text', 'urls'])

    for tweet in tweepy.Cursor(api.search, q= '#' + word + '-filter:retweets',
                                           count=100,
                                           lang="en",
                                           since=tstart,
                                           until=tend,
                                           tweet_mode='extended').items():
        print(tweet.created_at,' ',tweet.id)
        urls = tweet.entities['urls']
        cleaned = text_clean(tweet.full_text)
        if len(urls) >= 1:
            urls_list = []
            for i in range(len(urls)):
                urls_list.append(urls[i]['expanded_url'])
            row = [tweet.created_at, tweet.id, tweet.user.screen_name, cleaned, urls_list]
        else:
            row = [tweet.created_at, tweet.id, tweet.user.screen_name, cleaned]
        csvWriter.writerow(row)
    csvFile.close()
    
def download_delta_tweet_from_now(word,delta_tweetid):
    tweet = api.search(q=word)[0]
    initial_id = tweet.id - delta_tweetid
    print(tweet.id)
    print(initial_id)
    print()

    # Open/Create a file to append data
    csvFile = open(word + '.csv', 'a', newline='')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['tweet.created_at', 'tweet.id', 'tweet.user.screen_name', 'tweet.text', 'urls'])

    for tweet in tweepy.Cursor(api.search, q= '#' + word + '-filter:retweets',
                                           count=100,
                                           lang="en",
                                           since_id=initial_id,
                                           tweet_mode='extended').items():
        print(tweet.created_at,' ',tweet.id)
        urls = tweet.entities['urls']
        cleaned = text_clean(tweet.full_text)
        if len(urls) >= 1:
            urls_list = []
            for i in range(len(urls)):
                urls_list.append(urls[i]['expanded_url'])
            row = [tweet.created_at, tweet.id, tweet.user.screen_name, cleaned, urls_list]
        else:
            row = [tweet.created_at, tweet.id, tweet.user.screen_name, cleaned]
        csvWriter.writerow(row)
    csvFile.close()


# # Download data from twitter

# In[12]:


tstart        = '2019-10-01'
tend          = '2019-10-02'
delta_tweetid = 100000000000000000
search_word   = 'home'

# download tweets previous to the present one minus a delta
#download_delta_tweet_from_now(search_word,delta_tweetid)
# download tweets in a time delta (in days)
download_days(search_word,tstart,tend)


# # Find next word

# In[13]:


df_find = pd.read_csv(search_word + '.csv')
df_find.tail()


# In[15]:


words_stats = df_find['tweet.text'].str.split(expand=True).stack().value_counts()
words_list  = words_stats.keys().tolist()

filtered_list = [] 
for w in words_list: 
    if w.startswith('#'): 
        filtered_list.append(w)
filtered_list.remove('#')
#filtered_list.remove('#_')
filtered_stats = words_stats.filter(items = filtered_list)
        
print('# of words                ', len(words_stats))
print('# of words after filter   ', len(filtered_list))
print('# len of stas after filter', len(filtered_stats))
filtered_stats[0:5]


# In[ ]:





# In[ ]:





# In[ ]:




