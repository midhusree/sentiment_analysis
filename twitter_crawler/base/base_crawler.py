#!/usr/bin/env python
# -*- coding: utf-8 -*-
__maintainer__ = "Midhun Mohan"
import os


class BaseHandler:
    """
    class with acts as base for all types of crawler
    """
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    user_tweets_filename = "my_tweets.csv"
    user_specific_tweets_filename = "specific_user_tweets.csv"
    specific_tweets_filename = "specific_tweets.csv"
    user_tweets_foldername = "user_tweets_crawled"
    search_folder = "search_crawled"
    user_tweets_saver = os.path.join(
        base_path, "api_crawler", user_tweets_foldername, user_tweets_filename)
    specific_user_tweet = os.path.join(
        base_path, "api_crawler", user_tweets_foldername, user_specific_tweets_filename)
    specific_search = os.path.join(
        base_path, "api_crawler", search_folder, specific_tweets_filename)

    def __init__(self, ):
        os.makedirs(os.path.join(
            self.base_path, "api_crawler", self.user_tweets_foldername), exist_ok=True)
        os.makedirs(os.path.join(self.base_path, "api_crawler",
                                 self.search_folder), exist_ok=True)
