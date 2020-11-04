import praw
import random
import datetime
from textblob import TextBlob
import time

reddit = praw.Reddit('bot')

#source = reddit.subreddit('politics')
#destination = reddit.subreddit('csci040')

#url = 'https://www.reddit.com/r/csci040temp/comments/jk1bb9/trump_laboring_to_breathe_says_hes_fine_and/'
#submission = reddit.submission(url=url)

#ran the upvote and downvote extra credits within the bot.py file
"""
#running for extra credit 
for comment in all_comments:
    if 'biden' in comment.body.lower():
        comment.upvote()
print('upvoting comment')

#trying to run for extra credit
for comment in all_comments:
    if 'trump' in comment.body.lower():
        comment.downvote()
print('downvoting commment')

for comment in not_my_comments:
    blob = TextBlob(comment.body.lower())
    if 'biden' in comment.body.lower():
        #commentstr = str(comment)
        #print(commentstr)
        #print('biden = ', blob.sentiment.polarity)
        if blob.sentiment.polarity > 0:
            comment.upvote()
            #print('voting up for + biden')
        if blob.sentiment.polarity < 0: 
            comment.downvote()
            #print('voting down for - biden')
    if 'trump' in comment.body.lower():
        #print('trump = ', blob.sentiment.polarity)
        if blob.sentiment.polarity < 0: 
            comment.upvote()
            #print('voting up for - trump')
        if blob.sentiment.polarity > 0:
            comment.downvote()
            #print('voting down for + trump')

subreddit = reddit.subreddit('csci040temp')
for submission in subreddit.new(limit=None):
    sentence = TextBlob(submission.title.lower())
    if 'biden' in submission.title.lower():
        if sentence.sentiment.polarity > 0:
            submission.upvote()
        if sentence.sentiment.polarity < 0: 
            submission.downvote()
    if 'trump' in submission.title.lower():
        if sentence.sentiment.polarity < 0: 
            submission.upvote()
        if sentence.sentiment.polarity > 0:
            submission.downvote()

"""

#ran within this file
#Extra Credit: Have your bot post new submissions to the /r/csci040 subreddit. Post at least 20. (2 points)

for i in range(25):
    try:
        for submission in reddit.subreddit('politics').stream.submissions():
            if not submission.is_self:
                reddit.subreddit('csci040temp').submit(submission.title, url=submission.url)
    except praw.exceptions.RedditAPIException:
        print('exception found')
        time.sleep(60*60)
        print('done sleeping')

