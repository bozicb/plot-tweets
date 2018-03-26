import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
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

plt.hist([cl_tweets,sa_tweets,tr_tweets],stacked=True,label=['clinton','sanders','trum'])
plt.legend()
plt.title('Tweets mentioning each candidate')
plt.xlabel('Twitter account age in years')
plt.ylabel('# of tweets')
plt.annotate('More Trump tweets',xy=(1,35000),xytext=(2,35000),
             arrowprops=dict(facecolor='black'))
plt.show()

tweets['red']=tweets['user_bg_color'].apply(lambda x: colors.hex2color('#{0}'.format(x))[0])
tweets['blue']=tweets['user_bg_color'].apply(lambda x: colors.hex2color('#{0}'.format(x))[2])

fig,axes=plt.subplots(nrows=2,ncols=2)
ax0,ax1,ax2,ax3=axes.flat

ax0.hist(tweets['red'])
ax0.set_title('Red in backgrounds')
ax1.hist(tweets['red'][tweets['candidate']=='trump'].values)
ax1.set_title('Red in Trump tweeters')

ax2.hist(tweets['blue'])
ax2.set_title('Blue in backgrounds')
ax3.hist(tweets['blue'][tweets['candidate']=='trump'].values)
ax3.set_title('Blue in Trump tweeters')

plt.tight_layout()
plt.show()

tweets['user_bg_color'].value_counts()
