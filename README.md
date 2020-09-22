### **Sentiment Analysis**
The aim of this project is to analyses the sentiment of social media twitter data which help to improve the user experience over a social network or system interface. The learning algorithm will learn what are the emotions of the news data present in social media. Using sentiment analysis, we aim to provide excellent performance for real time news data on social media and also provide better results in terms of accuracy.

**Technology Used:**
Machine Learning Algorithm and Natural language processing

**Problem Statement**

The problem at hand consists of two subtasks:

- Sentiment Analysis in Twitter:

_Given a message containing a marked instance of a word or a phrase, determine whether that instance is positive, negative or neutral in that context._

-  Sentence Level Sentiment Analysis :

_Given a message, decide whether the message is of positive, negative, or neutral sentiment. For messages conveying both a positive and negative sentiment, whichever is the stronger sentiment should be chosen._


**GUI** 

![Picture2](https://user-images.githubusercontent.com/32463263/93847300-34eda300-fcc4-11ea-8c9f-e4b0e91ba993.png)

![Picture3](https://user-images.githubusercontent.com/32463263/93847314-3ae38400-fcc4-11ea-9248-f0f53f41ac4d.png)

![Picture4](https://user-images.githubusercontent.com/32463263/93847404-71210380-fcc4-11ea-8da7-ca7e40316187.png)

![Picture5](https://user-images.githubusercontent.com/32463263/93847408-754d2100-fcc4-11ea-990c-a92dcc48bd10.png)

![Picture6](https://user-images.githubusercontent.com/32463263/93847479-a3326580-fcc4-11ea-8c43-c96aca455a8c.png)

![Picture7](https://user-images.githubusercontent.com/32463263/93847486-a9c0dd00-fcc4-11ea-953c-54def10c22b8.png)

![Picture8](https://user-images.githubusercontent.com/32463263/93847538-c78e4200-fcc4-11ea-9abc-0ab2e2b592bf.png)

![Picture9](https://user-images.githubusercontent.com/32463263/93847544-cbba5f80-fcc4-11ea-8363-1bc8fa2b2748.png)

![Picture10](https://user-images.githubusercontent.com/32463263/93847560-d83eb800-fcc4-11ea-8973-2a6dcf135a8b.png)



**Code Snippet**

*Importing various Libraries and other Project Files such as Listed Below*

![image](https://user-images.githubusercontent.com/32463263/93846826-cbb96000-fcc2-11ea-93f6-49b5d6a816b7.png)

*Making A Splash Screen to Introduce the Application Name*



*Building a Root Window (container) as a Base Window*

![Picture11](https://user-images.githubusercontent.com/32463263/93847789-8f3b3380-fcc5-11ea-924d-05212e764a93.png)

*Extracting Tweets From Twitter*
```
`import tweepy

from tweepy.streaming import StreamListener

from tweepy import OAuthHandler

from tweepy import Stream

import json

import time

import pandas as pd
    
access_token = "1085460732727050241-HFKwiRJtEjFQcuFzLuIEQVo3072LPw"
access_secret = "L9ltIAi8F49ywLItCPPNMuQEOwkGOaqsYtVHgznX8Tf6S"
consumer_key = "z4b4IalHycnih8SB951QeSeCT"
consumer_secret = "6EcfdQmoppfZQzobMBUSREwLI4vBZTI8QFXnIWuy7Aepw2dyJS"
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
searchquery = s2
users =tweepy.Cursor(api.search,q=searchquery).items()
count = 0
start = 0
errorCount=0
waitquery = 100      #this is the number of searches it will do before resting
waittime = 2.0          # this is the length of time we tell our program to rest
total_number = 10   #this is the total number of queries we want
justincase = 1         #this is the number of minutes to wait just in case twitter throttles us
text = [1] * total_number
secondcount = 0  
`


```

*Naive bayes Classifier Implementation.*

![Picture13](https://user-images.githubusercontent.com/32463263/93847879-d9241980-fcc5-11ea-90b3-381cf5320af8.png)


*Plotting A Graph From Classifier Results*

![Picture14](https://user-images.githubusercontent.com/32463263/93847922-ef31da00-fcc5-11ea-873a-3751ec619707.png)


