# Twitter_Crawler
Crawling data from twitter using tweepy

> Notice: The crawler is meant to be used for collecting data purely for academic and research purpose only. I am not responsible for any legal issue that might arise for any unintended use of this crawler

Contains:
1. Crawling user timeline
2. Crawling user posts
3. Crawling based on a keyword



# How to run

    1. Clone the repo.
    2. Create a twitter developer account.
    3. Get tokens specified in .env_sample file.
    4. rename .env_sample to .env file & add the credentials 
    5. Build the code using docker and run the code using docker command

1.     docker build . -t twitter:0.1 --> it will setup the code on your local with all requirements installed.

2.     docker run -it twitter:0.1  --> We should be able to see the result in terminal as well, login to the container to see the csv file created with whole records
