#!/usr/bin/env python
# -*- coding: utf-8 -*-
__maintainer__ = "Midhun Mohan"


from twitter_crawler.api_crawler.user_tweets_crawler import UserCrawler
from twitter_crawler.api_crawler.crawl_search import SearchCrawler


if __name__ == "__main__":
    crawl = UserCrawler()
    crawl.get_my_timeline()
    user = input("Enter the user accountname: \t")
    crawl.get_specific_user_timeline(user)
    search_crawl = SearchCrawler()
    query = input("Enter the search string : \t")
    search_crawl.search_on_twitter(query)
