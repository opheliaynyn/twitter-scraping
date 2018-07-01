import get_tweet_conversation as gtc
import re


if __name__ == '__main__':
    tl = gtc.search_global_timeline('2018-06-26', '2018-06-28')
    for tweet in tl['statuses']:
        try:
            id = tweet['in_reply_to_status_id']
            tweet_parent = gtc.get_tweet_filter_id(id)
            print(tweet['in_reply_to_status_id'])
            print(re.sub('@[!-~]+ ', '', tweet_parent['text'], 100))
            print("-")
            print(tweet['id'])
            print(re.sub('@[!-~]+ ', '', tweet['text'], 100))
        except Exception as e:
            pass

        print("*****************")
