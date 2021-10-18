# Twitterscraper
My task was to identify power outages with social media. With the ultimate goal of improving the ability of emergency management officials to allocate resources in real-time.

I identified Twitter as the platform most likely to yield a large number of posts related to the subject, and enthusiastically set out to begin collecting tweets.

My enthusiasm was tested, however, as I ran into several stumbling blocks.

The first logical choice was to use Twitter’s official Search api. Unfortunately, the free version only allows access to the seven most recent days of historical tweets and is limited to scraping 18,000 tweets per a 15-minute window.

With further access requiring a costly subscription. Since I did not have the resources to buy a subscription, there was no way this method would allow me to amass enough data to train a model.

Next, I tried the Tweetscraper package. This seemed promising, and, indeed, I got excellent results with Tweetscraper.

Unfortunately for me, I overtaxed the API during my initial experimentation with using the package, and my computers were locked out from further access before I could refine my query to get meaningful results.

This was a major bummer, but the deadline loomed and we still had our hearts set on using Twitter. Enter Twitterscraper!

Twitterscraper doesn’t have the same built-in Python functionality that Tweetscraper does, so, first I have to install the package, to run my initial queries.
