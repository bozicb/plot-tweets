import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

tweets=pd.read_csv("tweets.csv")
tweets['created']=pd.to_datetime(tweets['created'])
tweets['user_created']=pd.to_datetime(tweets['user_create'])
tweets['user_age']=tweets['user_created'].apply(
    lambda x: (datetime.now()-x).total_seconds()/3600/24/365)

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
plt.bar(range(len(counts)),counts)
plt.show()
print(counts)

plt.hist(tweets['user_age'])
plt.show
