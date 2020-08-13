import os
from tweepy.auth import OAuthHandler
from tweepy.api import API
from dotenv import load_dotenv
load_dotenv(verbose=True)


class TweepyAuth:
    """
    class used to handle app authentication
    """
    consumer_key = os.getenv("API_KEY")
    consumer_secret = os.getenv("API_SECRET_KEY")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    @property
    def authenticate(self):
        """
        method to authenticate the application
        """
        # Creating the authentication object
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        # Setting your access token and secret
        auth.set_access_token(self.access_token, self.access_token_secret)
        # Creating the API object while passing in auth information
        api = API(auth, wait_on_rate_limit=True,
                  wait_on_rate_limit_notify=True)
        return api

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        else:
            return api
