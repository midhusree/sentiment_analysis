#!/usr/bin/env python
# -*- coding: utf-8 -*-

__maintainer__ = "Midhun Mohan"

import os
import collections
import pandas as pd

from twitter_crawler.base.tweepy_auth import TweepyAuth
from twitter_crawler.base.base_crawler import BaseHandler


class SearchCrawler(BaseHandler, TweepyAuth):
    """
    Class used to crawl records of a search key using tweepy API
    """

    def __init__(self):
        super().__init__()

    def search_on_twitter(self, search_key):
        """
        Method used to search on twitter for a particular keyword and get result
        """
        language = "en"
        user_records = collections.defaultdict(list)
        # Using the API object to get tweets from searcg, and storing it in a variable called search_records
        search_records = self.authenticate.search(q=search_key, lang=language)
        # loop through all tweets pulled

        print(f"getting  tweets from search key {search_key}")
        for tweet in search_records:
            # printing the text stored inside the tweet object
            user_records["tweeted_user"].append(tweet.user.screen_name)
            user_records["tweeted_user_location"].append(tweet.user.location)
            user_records["tweeted_created_at"].append(tweet.created_at)
            user_records["tweeted_text"].append(tweet.text)
        print("Generating dataframe")
        user_records_df = pd.DataFrame(user_records)
        print(user_records_df.head())
        print(f"saving records to CSV {self.specific_search}")
        user_records_df.to_csv(self.specific_search,
                               sep=',', encoding='utf-8', index=False)
        return
