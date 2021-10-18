#Importing necessary files
from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

#Providing the range of days in which I want the data 
begin_date=dt.date(2020,4,1)
end_date=dt.date(2020,4,3)

#Providing limit to the fetched tweets and also specifying the language of the desired tweets
limit=1000
language='english'

#Extracting tweets for the Keyword “Covid-19”
tweets=query_tweets("Covid-19”,limit=limit,
    begindate=begin_date,
    enddate=end_date,lang=language)
    #Creating Dataframe for the extracted tweets
df=pd.DataFrame(t.__dict__ for t in tweets)
df.head()
