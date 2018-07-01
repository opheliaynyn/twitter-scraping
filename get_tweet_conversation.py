import config
from requests_oauthlib import OAuth1Session
import json

CONSUMER_KEY = config.MY_CONSUMER_KEY
CONSUMER_SECRET = config.MY_CONSUMER_SECRET
ACCESS_KEY = config.MY_ACCESS_KEY
ACCESS_SECRET = config.MY_ACCESS_SECRET

URL_HOME_TIMELINE = "https://api.twitter.com/1.1/statuses/home_timeline.json"
URL_SEARCH = "https://api.twitter.com/1.1/search/tweets.json"
URL_SHOW = "https://api.twitter.com/1.1/statuses/show.json"


def connect_oauth():
    oauth = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET,
                          ACCESS_KEY, ACCESS_SECRET)
    return oauth


def search_global_timeline(since, until):
    params = {
        "q": 'filter:replies since:' + since + ' until:' + until,
        "lang": "ja",
        "count": 200,
    }

    oauth = connect_oauth()
    res = oauth.get(URL_SEARCH, params=params)
    timeline = json.loads(res.text)

    return timeline


def get_home_timeline(since, until):
    params = {
        "q": 'filter:replies since:' + since + ' until:' + until,
        "lang": "ja",
        "count": 100,
        "include_rts": False,
    }

    oauth = connect_oauth()
    res = oauth.get(URL_HOME_TIMELINE, params=params)
    timeline = json.loads(res.text)

    return timeline


def get_tweet_filter_id(id):
    params = {
        "id": id,
    }

    oauth = connect_oauth()
    res = oauth.get(URL_SHOW, params=params)
    timeline = json.loads(res.text)

    return timeline
