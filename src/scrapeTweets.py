import snscrape.modules.twitter as sntwitter
import pandas as pd

maxTweets = 200000
tweetList = []
tweetListTest = [1]
tweetDFTest = pd.DataFrame(tweetListTest)
tweetDFTest.to_csv("../data/raw/test.csv")

for i, tweet in enumerate(sntwitter.TwitterSearchScraper('cardano since:2021-06-01 until:2021-09-01').get_items()):
    if i > maxTweets:
        break
    tweetList.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

tweetDF = pd.DataFrame(tweetList, columns=['Datetime', 'Tweet ID', "Text", "User"])

tweetDF.to_csv("../data/raw/tweetsRaw.csv")

