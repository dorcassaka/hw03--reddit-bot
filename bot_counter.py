
import praw

# FIXME:
# edit this line to contain your bot's username
username = 'botdessert'

# FIXME:
# the praw instance needs access to a valid praw.ini file 
# with a login credentials section called "bot"
reddit = praw.Reddit('bot')
redditor = reddit.redditor(name = username)

# calculate and print the total number of comments that username has created
comments = list(redditor.comments.new(limit=None))
print("len(comments)=",len(comments))

# calculate and print the total number of top level comments and the total number of replies
top_level_comments = []
replies = []
for comment in comments:
    try:
        if type(comment.parent()) is praw.models.Submission:
            top_level_comments.append(comment)
        else:
            replies.append(comment)
    except AttributeError:
        pass
print("len(top_level_comments)=",len(top_level_comments))
print("len(replies)=",len(replies))

# calculate the number of valid top level comments
parents = []
for reply in top_level_comments:
    parents.append(reply.parent().id)
valid_top_level_comments = []
for reply in top_level_comments:
    if parents.count(reply.parent().id) == 1:
        valid_top_level_comments.append(reply)
print("len(valid_top_level_comments)=",len(valid_top_level_comments))

# calculate the number of replies that are not replying to themselves
not_self_replies = []
for reply in replies:
    try:
        if reply.parent().author.name!=username:
            not_self_replies.append(reply)
    except AttributeError:
        pass
print("len(not_self_replies)=",len(not_self_replies))

# calculate the number of valid replies;
# that is, replies that are not replying to themselves,
# and that are not duplicate replies to the same parent comment
parents = []
for reply in not_self_replies:
    try:
        parents.append(reply.parent().id)
    except AttributeError:
        pass
valid_replies = []
for reply in not_self_replies:
    try:
        if parents.count(reply.parent().id) == 1:
            valid_replies.append(reply)
    except AttributeError:
        pass
print("len(valid_replies)=",len(valid_replies))

# the total number of valid comments is the number of valid top level comments 
# plus the number of valid replies
valid_comments = len(valid_replies) + len(valid_top_level_comments)
print('========================================')
print("valid_comments=",valid_comments)
print('========================================')
print('NOTE: the number valid_comments is what will be used to determine your extra credit')


#726 @ 5:21 pm 10/28

"""
len(comments)= 1000
len(top_level_comments)= 22
len(replies)= 978
len(valid_top_level_comments)= 22
len(not_self_replies)= 978
len(valid_replies)= 686
========================================
valid_comments= 708 @ 1:40 am 10/29
========================================

len(comments)= 1000
len(top_level_comments)= 39
len(replies)= 961
len(valid_top_level_comments)= 39
len(not_self_replies)= 961
len(valid_replies)= 667
========================================
valid_comments= 706 @ 12:11 pm 10/29
========================================

len(comments)= 1000
len(top_level_comments)= 97
len(replies)= 903
len(valid_top_level_comments)= 97
len(not_self_replies)= 903
len(valid_replies)= 877
========================================
valid_comments= 974 @ 2:48 am 10/30
========================================

len(comments)= 1000
len(top_level_comments)= 99
len(replies)= 901
len(valid_top_level_comments)= 99
len(not_self_replies)= 901
len(valid_replies)= 883
========================================
valid_comments= 982 @ 3:16 am 10/30
========================================

len(comments)= 1000
len(top_level_comments)= 44
len(replies)= 956
len(valid_top_level_comments)= 42
len(not_self_replies)= 956
len(valid_replies)= 948
========================================
valid_comments= 990 @ 12:50 pm 10/30
========================================

len(comments)= 1000
len(top_level_comments)= 37
len(replies)= 963
len(valid_top_level_comments)= 35
len(not_self_replies)= 962
len(valid_replies)= 948
========================================
valid_comments= 983  @ 4:47 pm 10/30
========================================

len(comments)= 1000
len(top_level_comments)= 36
len(replies)= 964
len(valid_top_level_comments)= 34
len(not_self_replies)= 963
len(valid_replies)= 953
========================================
valid_comments= 987 @ 7:30 ppm 10/30
========================================

len(comments)= 1000
len(top_level_comments)= 61
len(replies)= 939
len(valid_top_level_comments)= 59
len(not_self_replies)= 938
len(valid_replies)= 928
========================================
valid_comments= 987 @ 12:30 am 10/31
========================================

len(comments)= 1000
len(top_level_comments)= 183
len(replies)= 817
len(valid_top_level_comments)= 181
len(not_self_replies)= 816
len(valid_replies)= 806
========================================
valid_comments= 987 @12:20 am 11/1
========================================

Dorcass-Air:reddit_bot dorcassaka$ /usr/local/bin/python3 /Users/dorcassaka/Downloads/reddit_bot/bot_counter.py
len(comments)= 1000
len(top_level_comments)= 245
len(replies)= 755
len(valid_top_level_comments)= 243
len(not_self_replies)= 755
len(valid_replies)= 749
========================================
valid_comments= 992 @ 9:34 pm 11/1
========================================

len(comments)= 1000
len(top_level_comments)= 279
len(replies)= 721
len(valid_top_level_comments)= 277
len(not_self_replies)= 721
len(valid_replies)= 715
========================================
valid_comments= 992 @ 2:25 am 11/03 
========================================

len(comments)= 1000
len(top_level_comments)= 279
len(replies)= 721
len(valid_top_level_comments)= 277
len(not_self_replies)= 721
len(valid_replies)= 715
========================================
valid_comments= 992 @ 2:45 pm 11/03
========================================
"""