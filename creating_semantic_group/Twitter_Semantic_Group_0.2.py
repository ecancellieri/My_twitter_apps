#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tweepy import OAuthHandler
import tweepy
import csv
import pandas as pd
import re
from datetime import date
import os


# In[4]:


today = date.today()
print("Today's date                    :", today)


# detect the current working directory and create date directory
path = os.getcwd()
path = path + '\\' + str(today)

print ("The current working directory is: %s" % path)
try:
    os.mkdir(path)
except OSError:
    print ("Failed to create directory      : %s" % path)
else:
    print ("Successfully created directory  : %s " % path)


# In[5]:


# Twitter user application details needed to connect to the Twitter API.
consumer_key = "XXX"
consumer_secret = "YYY"
access_token = "WWW"
access_token_secret = "ZZZ"


# In[6]:


# Set up the API connection and test authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# In[7]:


# Creates the user object. The me() method returns the user whose authentication keys were used.
user = api.me()
 
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))


# In[9]:


def text_clean(inputString):
    out_string = inputString.encode('ascii', 'ignore').decode('ascii')
    out_string = re.sub(r"http\S+"  , '', out_string.lower())
    out_string = re.sub('@[^\s]+'   , '', out_string.lower())
    out_string = re.sub('[!?,.:";-]', '', out_string)
    out_string = re.sub('\d+'       , '', out_string)
    out_string = re.sub('\n'        , '', out_string)
    return out_string

def download_days(path, word,day1,day2):
    # Open/Create a file to append data
    csvFile = open(path + '\\' + word + '.csv', 'a', newline='')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['tweet.created_at', 'tweet.id', 'tweet.user.screen_name', 'tweet.text', 'urls'])

    for tweet in tweepy.Cursor(api.search, q= '#' + word + '-filter:retweets',
                                           count=100,
                                           lang="en",
                                           since=tstart,
                                           until=tend,
                                           tweet_mode='extended').items():
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
    
def download_delta_tweet_from_now(path, word,delta_tweetid):
    tweet = api.search(q=word)[0]
    initial_id = tweet.id - delta_tweetid

    # Open/Create a file to append data
    csvFile = open(path + '\\' + word + '.csv', 'a', newline='')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['tweet.created_at', 'tweet.id', 'tweet.user.screen_name', 'tweet.text', 'urls'])

    for tweet in tweepy.Cursor(api.search, q= '#' + word + '-filter:retweets',
                                           count=100,
                                           lang="en",
                                           since_id=initial_id,
                                           tweet_mode='extended').items():
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

def find_word_ranking(df):
    words_stats   = df['tweet.text'].str.split(expand=True).stack().value_counts()
    words_ranking = words_stats.keys().tolist()

    filtered_list = [] 
    for w in words_ranking: 
        if w.startswith('#'): 
            filtered_list.append(w)
    if '#'  in filtered_list: filtered_list.remove('#' )
    if '#_' in filtered_list: filtered_list.remove('#_')
    filtered_stats = words_stats.filter(items = filtered_list)
    out_word = filtered_stats.keys()[1][1:]
    
    print('# of words                :', len(words_stats))
    print('# of words after filter   :', len(filtered_list))
    print('# len of stas after filter:', len(filtered_stats))
    print('Highest ranging word      :', out_word)
    print()
    return out_word


# # Download data from twitter

# In[9]:


tstart     = '2019-10-14'
tend       = '2019-10-15'
delta_tweetid = 10000000000000
start_word = 'furniture'



flag        = 0
word_list   = [start_word]
search_word = word_list[-1]
while flag == 0:
    print('Search word:', search_word)
    #download_delta_tweet_from_now(path, search_word,delta_tweetid)
    download_days(path, search_word, tstart, tend)
    df_find = pd.read_csv(path + '\\' + search_word + '.csv')
    search_word = find_word_ranking(df_find)
    if search_word not in word_list:
        word_list.append(search_word)
        print('New list  ', word_list)
    else:
        flag = 1
        print('Final list', word_list)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




