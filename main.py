import json
from twython import Twython, TwythonError
import pandas as pd
import plotly_express as px
import argparse

#define arguments
ap = argparse.ArgumentParser()
ap.add_argument("--keyword", required = True,
help ='Search keyword to retrieve tweets')
ap.add_argument("--count", required = True,
help ='Number of tweets to retrieve') 
ap.add_argument("--language", default = 'en')  
args = vars(ap.parse_args())

#load twitter app credentials from json file
with open (r"twitter_credentials.json", "r") as file:
    creds=json.load(file)

#instantiate a Twython object with your credentials
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

#create a query
query = {'q': args['keyword'],
        'result_type': 'popular',
        'count': args['count'],
        'lang': args['language']
}

#search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'fav_count': [],
'retweeted': [], 'retweet_count': [], 'tweet_length': []
}

for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['fav_count'].append(status['favorite_count'])
    dict_['retweeted'].append(status['retweeted'])
    dict_['retweet_count'].append(status['retweet_count'])
    dict_['tweet_length'].append(len(status['text']))

#create a dataframe with the information 
df = pd.DataFrame(dict_)
print(df)

#Visualization of tweet_length vs retweet_count
fig = px.scatter(df, x = "tweet_length", y = "retweet_count")
fig.write_html('Tweet length vs Retweet Count.html')



