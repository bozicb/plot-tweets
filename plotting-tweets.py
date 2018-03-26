import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

tweets=pd.read_csv("tweets.csv")
tweets['created']=pd.to_datetime(tweets['created'])
tweets['user_created']=pd.to_datetime(tweets['user_created'])
tweets['user_age']=tweets['user_created'].apply(
    lambda x: ((datetime.now()-x).total_seconds()/3600/24/365)-2)

def get_candidate(row):
    candidates=[]
    text=row['text'].lower()
    if 'clinton' in text or 'hillary' in text:
        candidates.append('clinton')
    if 'trump' in text or 'donald' in text:
        candidates.append('trump')
    if 'sanders' in text or 'bernie' in text:
        candidates.append('sanders')
    return ','.join(candidates)

tweets['candidate']=tweets.apply(get_candidate,axis=1)
counts=tweets['candidate'].value_counts()

cl_tweets=tweets['user_age'][tweets['candidate']=='clinton']
sa_tweets=tweets['user_age'][tweets['candidate']=='sanders']
tr_tweets=tweets['user_age'][tweets['candidate']=='trump']

plt.hist([cl_tweets,sa_tweets,tr_tweets],stacked=True,
         label=['clinton','sanders','trum'])
plt.legend()
plt.title('Tweets mentioning each candidate')
plt.xlabel('Twitter account age in years')
plt.ylabel('# of tweets')
plt.annotate('More Trump tweets',xy=(1,35000),xytext=(2,35000),
             arrowprops=dict(facecolor='black'))
plt.show()
