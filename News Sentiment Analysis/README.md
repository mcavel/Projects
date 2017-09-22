
<Center><h1>News Sentiment Analysis</h1></center>

<img src="nsa.jpg">




```python
# Dependencies
import tweepy
import json
import numpy as np
import time
import pandas as pd
import time
from matplotlib import pyplot as plt
import seaborn as sns
import csv
import os
from config import ck, cs, at, ats

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys 
consumer_key = ck
consumer_secret =cs
access_token = at
access_token_secret = ats

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

```


```python
# Target Search Term
target_terms = ("@BBCNews", "@CBSNews", "@CNN", "@FoxNews", "@nytimes")

# List for tweet data
table_dict = []
# Loop through all targets
for target in target_terms:
    counter=101
    public_tweets = api.user_timeline(target, count=100, result_type="recent")
#     tweetstorage[target]= public_tweets
    for tweet in public_tweets:

        # Run VAnalysis on each tweet
        compound = analyzer.polarity_scores(tweet["text"])["compound"]
        pos = analyzer.polarity_scores(tweet["text"])["pos"]
        neu = analyzer.polarity_scores(tweet["text"])["neu"]
        neg = analyzer.polarity_scores(tweet["text"])["neg"]
        tweetorder=counter-1
        counter=counter-1
        #Temp store other values
        date=time.strftime('%m/%d/%Y', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
        text=(tweet["text"])
        name=(tweet["user"]["name"])

        #append value to DataFrame
        table_dict.append({"Media Sources":name,"Tweet Polarity":compound,"Positive":pos,"Neutral":neu,
                          "Date":date,"Text":text,"Tweets Ago":tweetorder})
        
table_dict=pd.DataFrame(table_dict)
table_dict.head()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Media Sources</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Text</th>
      <th>Tweet Polarity</th>
      <th>Tweets Ago</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>09/21/2017</td>
      <td>BBC News (UK)</td>
      <td>0.686</td>
      <td>0.000</td>
      <td>House of Lords rejects 'flawed' expenses repor...</td>
      <td>-0.4939</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>09/21/2017</td>
      <td>BBC News (UK)</td>
      <td>0.446</td>
      <td>0.000</td>
      <td>Boy, 17, arrested over Tube attack https://t.c...</td>
      <td>-0.7351</td>
      <td>99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>09/21/2017</td>
      <td>BBC News (UK)</td>
      <td>0.672</td>
      <td>0.000</td>
      <td>James Herbert death: Watchdog makes police res...</td>
      <td>-0.5994</td>
      <td>98</td>
    </tr>
    <tr>
      <th>3</th>
      <td>09/20/2017</td>
      <td>BBC News (UK)</td>
      <td>0.882</td>
      <td>0.000</td>
      <td>Quit smoking campaign Stoptobber backs e-cigs ...</td>
      <td>-0.0516</td>
      <td>97</td>
    </tr>
    <tr>
      <th>4</th>
      <td>09/20/2017</td>
      <td>BBC News (UK)</td>
      <td>0.598</td>
      <td>0.231</td>
      <td>Chronic fatigue therapy 'could help teenagers'...</td>
      <td>0.1779</td>
      <td>96</td>
    </tr>
  </tbody>
</table>
</div>




```python
#create lmplot using seasborn
#set colorlist for charts
clrlist = ["#82CAFA", "#438D80", "#FF0000", "#0000FF", "#FFFF00"]
sns.set_palette(clrlist)

#create chart
MediaTweetAnalysis=sns.lmplot(x="Tweets Ago", y="Tweet Polarity", data= table_dict, 
           hue="Media Sources",  size=7, aspect=1.4 ,
           legend_out = True, legend = False, 
           scatter_kws={"s":150, 
                        'alpha':.55,'edgecolors':"black", 'linewidth':1},ci=0, fit_reg=False, )

plt.xlim(102,-2)
plt.title("Sentiment Analysis of Media Tweets ("+str(table_dict["Date"][2])+")", fontsize=18)
plt.legend(bbox_to_anchor=(1, 1), loc='upper left', ncol=1, title="Media Sources")
plt.savefig("Output/NSA_MediaTweets.png", bbox_inches='tight')
plt.show(MediaTweetAnalysis)

```


![png](output_3_0.png)



```python
#create dataframe for using groupby
table_dict1 = pd.DataFrame(table_dict.groupby(["Media Sources"])["Tweet Polarity"].mean()).reset_index()
table_dict1
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Media Sources</th>
      <th>Tweet Polarity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BBC News (UK)</td>
      <td>-0.156798</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CBS News</td>
      <td>-0.068770</td>
    </tr>
    <tr>
      <th>2</th>
      <td>CNN</td>
      <td>0.024572</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Fox News</td>
      <td>0.001959</td>
    </tr>
    <tr>
      <th>4</th>
      <td>The New York Times</td>
      <td>-0.017140</td>
    </tr>
  </tbody>
</table>
</div>




```python
#create barplot using seaborn
MediaSent_O=sns.barplot(x="Media Sources", y="Tweet Polarity", data=table_dict1)
plt.ylim(-.2,.1)
plt.ylabel('Tweet Polarity')
plt.title("Overall Media Sentiment based on Twitter ("+str(table_dict["Date"][2])+")", fontsize=18)
plt.savefig("Output/NSA_OverallSentiment.png", bbox_inches='tight')
plt.show(MediaSent_O)

```


![png](output_5_0.png)



```python
#export dataframe to csv file
table_dict.to_csv('Output/newsanalysis.csv', index=False)

```
