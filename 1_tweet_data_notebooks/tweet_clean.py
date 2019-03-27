import pandas as pd
import numpy as np

def deefify2(tweet_raw):
    outlist = []
    
    for tweet in tweet_raw:
        temp_list = [tweet['id'],
                     tweet['user']['id'],
                     tweet['user']['name'],
                     tweet['user']['screen_name'],
                     tweet['created_at'],
                     tweet['full_text'],
                     tweet['favorite_count'],
                     tweet['retweet_count'],
                     tweet['user']['followers_count'],
                     tweet['user']['verified'],
                     tweet['in_reply_to_status_id'],
                     tweet['in_reply_to_user_id'],
                     tweet['in_reply_to_screen_name']]
        try:
            temp_list.append(tweet['retweeted_status']['full_text'])
        except:
            temp_list.append(np.nan)
            
        try:
            temp_list.append(tweet['retweeted_status']['id'])
        except:
            temp_list.append(np.nan)

        try:
            temp_list.append(tweet['retweeted_status']['user']['id'])
        except:
            temp_list.append(np.nan)
        
        try:
            temp_list.append(tweet['retweeted_status']['user']['screen_name'])
        except:
            temp_list.append(np.nan)
            
        try:
            temp_list.append(tweet['retweeted_status']['user']['verified'])
        except:
            temp_list.append(np.nan)
            
        try:
            temp_list.append(tweet['retweeted_status']['favorite_count'])
        except:
            temp_list.append(np.nan)

        try:
            temp_list.append(tweet['retweeted_status']['user']['followers_count'])
        except:
            temp_list.append(np.nan)         
            
        try:
            temp_list.append(tweet['quoted_status']['full_text'])
        except:
            temp_list.append(np.nan)
            
        try:
            temp_list.append(tweet['quoted_status']['id'])
        except:
            temp_list.append(np.nan)

        try:
            temp_list.append(tweet['quoted_status']['user']['id'])
        except:
            temp_list.append(np.nan)
        
        try:
            temp_list.append(tweet['quoted_status']['user']['screen_name'])
        except:
            temp_list.append(np.nan)
            
        try:
            temp_list.append(tweet['quoted_status']['user']['verified'])
        except:
            temp_list.append(np.nan)
            
        try:
            temp_list.append(tweet['quoted_status']['favorite_count'])
        except:
            temp_list.append(np.nan)
        outlist.append(temp_list)
    
    '''
    tweet_id is the tweet's specific ID (each tweet is unique)
    user_id is each user's specific ID (each user's ID is unique). This is what we can use to link users
    display_name is a user's display name, which can be changed easily and doens't need to be unique. screen_name is unique
    main_text is the text of a tweet. If it's a retweet, it will be stored here, as well as retweet_text, but here, it is truncated
    retweet_text is original tweet, non-truncated
    retweet_id is retweet's tweet_id
    retweet_user_id is the user who was re-tweeted's ID
    retweet_screen_name, obvious
    Same as above for quoted tweets
    not doing coordinates, not enough data there
    '''
    column_names = ['tweet_id',
                    'user_id',
                    'display_name',
                    'screen_name',
                    'tweet_date',
                    'main_text',
                    'fav_count',
                    'rt_count',
                    'followers_count',
                    'is_verified',
                    'reply_to_tweet_id',
                    'reply_to_user_id',
                    'reply_to_screen_name',
                    'retweet_text',
                    'retweet_id',
                    'retweet_user_id',
                    'retweet_screen_name',
                    'retweet_is_verified',
                    'retweet_fav_count',
                    'retweet_followers_count',
                    'quoted_text',
                    'quoted_id',
                    'quoted_user_id',
                    'quoted_screen_name',
                    'quoted_is_verified',
                    'quoted_fav_count']
    
    df_temp = pd.DataFrame(outlist, columns = column_names)
    
    df_temp['is_retweet'] = np.where((df_temp['retweet_text'].isnull()), 0, 1)
    df_temp['is_quote'] = np.where((df_temp['quoted_text'].isnull()), 0, 1)
    return df_temp