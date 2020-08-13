#!/usr/bin/env python
# -*- coding: utf-8 -*-

__maintainer__ = "Midhun Mohan"

import os
import collections
import pandas as pd

from twitter_crawler.base.tweepy_auth import TweepyAuth
from twitter_crawler.base.base_crawler import BaseHandler


class UserCrawler(BaseHandler, TweepyAuth):
    """
    Class used to crawl records of user using tweepy API
    """

    def __init__(self):
        super().__init__()

    def get_my_timeline(self):
        """
        Method used to get the developer account user timeline details, for demo we are here recording
        few data we get back. It has more record to display and use.
        """

        user_records = collections.defaultdict(list)
        # Using the API object to get tweets from your timeline, and storing it in a variable called my_tweets
        my_tweets = self.authenticate.home_timeline(count=25)
        # loop through all tweets pulled

        print("getting 25 tweets from my timeline")
        for tweet in my_tweets:
            # printing the text stored inside the tweet object
            user_records["tweeted_user"].append(tweet.user.screen_name)
            user_records["tweeted_user_location"].append(tweet.user.location)
            user_records["tweeted_created_at"].append(tweet.created_at)
            user_records["tweeted_text"].append(tweet.text)
        print("Generating dataframe")
        user_records_df = pd.DataFrame(user_records)
        print(user_records_df.head())
        print(f"saving records to CSV {self.user_tweets_saver}")
        user_records_df.to_csv(self.user_tweets_saver,
                               sep=',', encoding='utf-8', index=False)
        return

    def get_specific_user_timeline(self, username):
        """
        Method to handle specific user timeline record

        """
        user_records = collections.defaultdict(list)
        # Calling the user_timeline function with our parameters
        results = self.authenticate.user_timeline(id=username, count=25)

        print(f"getting 25 tweets of  {username}'s timeline")
        for i, tweet in enumerate(results):
            user_records["tweeted_user"].append(tweet.user.name)
            user_records["screen_name"].append(tweet.user.screen_name)
            user_records["tweeted_user_location"].append(tweet.user.location)
            user_records["tweeted_user_profile_image_url"].append(
                tweet.user.profile_image_url_https)
            user_records["tweeted_user_description"].append(
                tweet.user.description)
            user_records["followers_count"].append(tweet.user.followers_count)
            user_records["friends_count"].append(tweet.user.friends_count)
            user_records["tweeted_text"].append(tweet.text)
            user_records["retweet_count"].append(tweet.retweet_count)
            user_records["favorite_count"].append(tweet.favorite_count)
            user_records["favorited"].append(tweet.favorited)
            user_records["retweeted"].append(tweet.retweeted)
            user_records["lang"].append(tweet.lang)
            user_records["tweeted_created_at"].append(tweet.created_at)

        print("Generating dataframe")
        user_records_df = pd.DataFrame(user_records)
        print(user_records_df.head())
        print(f"saving records to CSV {self.specific_user_tweet}")
        user_records_df.to_csv(self.specific_user_tweet,
                               sep=',', encoding='utf-8', index=False)

        return
