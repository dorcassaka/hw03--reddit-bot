import praw
import random
import datetime
from textblob import TextBlob
import time


# FIXME:
# copy your generate_comment functions from the week_07 lab here
def generate_comment_0():
    names = ['Biden', 'Joe', 'Joe Biden', 'Vice President', 'Joseph', 'Joseph Robinette Biden Jr', 'Big Joe']
    name = random.choice(names)
    verbs = ['will be', 'should be', 'can be', 'is going to be', 'will soon be'] 
    verb = random.choice(verbs)
    jobs = ['the president', 'the 46th president', 'the leader', 'the head', 'the chief']
    job = random.choice(jobs)
    countries = ['of the US', 'of the United States', 'of the best country in the world', 'of the USA', 'of the United States of America']
    country = random.choice(countries)
    purposes = ['vote.', 'make a plan to vote.', 'donate to his campaign.', 'help his campaign.', 'participate in the election.', 'phone bank for Joe.']
    purpose = random.choice(purposes)

    text = name + " " + verb + " " + job + " " + country + ". It is your duty to " + purpose 
    return text

def generate_comment_1():
    names2 = ['Biden', 'Joe', 'Joe Biden', 'Vice President', 'Joseph', 'Joseph Robinette Biden Jr', 'Big Biden']
    name2 = random.choice(names2)
    beliefs = ['climate change', 'climate emergency', 'global heating', 'global warming', 'climate crisis']
    belief = random.choice(beliefs)
    nouns = ['He', 'His team', 'His administration', 'His squad', 'His crew', 'His party']
    noun = random.choice(nouns)
    verbs2 = ['will support', 'supports', 'backs', 'helps pass', 'pushes']
    verb2 = random.choice(verbs2)
    bills = ['bills', 'laws', 'legislation', 'charters', 'acts']
    bill = random.choice(bills)

    text = name2 + " believes in " + belief + ". " + noun + " "+ verb2 + " "+ bill + " that fight for our planet."
    return text

def generate_comment_2():
    names3 = ['Biden', 'Daddy Joe', 'Joe Biden', 'Vice President', 'Joseph', 'Joseph Robinette Biden Jr']
    name3 = random.choice(names3)
    whys = ['strengthen labor and workers’ rights.', 'fight for good jobs and worker protections.', 'advocate for the health of workers and their families.', 'rebuild the economy.', 'prepare for pandemics.', 'support unions.']
    why = random.choice(whys)
    peoples = ['We', 'Americans', 'The people', 'Great Americans', 'Fellow-Citizens']
    people = random.choice(peoples)
    needs = ['need', 'require', 'desire', 'want', 'long for']
    need = random.choice(needs)
    adjectives = ['good', 'great', 'better', 'noble', 'serious', 'stupendous']
    adjective = random.choice(adjectives)

    text = "Vote for " + name3 + " because he will " + why + " "+ people+ " " + need + " a " + adjective + " president."
    return text

def generate_comment_3():
    names4 = ['Donald', 'Trump', 'Donald Trump', 'Orange Man', 'Pig Donald', '45']
    name4 = random.choice(names4)
    trashing = ['trash.', 'rubbish.', 'a scum.', 'garbage.', 'junk.']
    trash = random.choice(trashing)
    verbs3 = ['killed', 'murdered', 'destroyed', 'slaughtered', 'wiped out']
    verb3 = random.choice(verbs3)
    when2 = ['the pandemic.', 'COVID.', 'Corona.', 'the virus outbreak.', 'Coronavirus.']
    when = random.choice(when2)
    hows = ['trust', 'like', 'love', 'want', 'desire']
    how = random.choice(hows)
    text = name4 + " is " + trash + " He " + verb3 + " hundreds of thousands of people during " + when + " How can you " + how + " him as a president?" 
    return text

def generate_comment_4():
    names5 = ['Donald', 'Trump', 'Donald Trump', 'Orange Man', 'Pig Donald', '45']
    name5 = random.choice(names5)
    words = ['racist.', 'sexist.', 'homophobic.', 'elitist.', 'transphobic.', 'corrupt.']
    word = random.choice(words)
    descriptions = ['The umpa lumpa', 'The Cheeto', 'The Angry Creamsicle', 'Captain Chaos', 'Orange Julius', 'The Screaming Carrot Demon', 'Trumplethinskin', 'Tiny Hands']
    description = random.choice(descriptions)
    hates = ['women.', 'men.', 'Americans.', 'immigrants.', 'you.', 'your mom.', 'your best friend.', 'your family.', 'your face.']
    hate = random.choice(hates)
    nows = ['Save yourself.', 'Save your family.', 'Do not vote for him.', 'Move to a different country.', 'Tell your friends.', 'Tell your family.']
    now = random.choice(nows)
    reminders = ['He was impeached.', 'He has destroyed the economy.', 'He does not support the black lives matter movement.', 'He does not wear masks.', 'He tested positive for COVID.', 'He almost started World War 3.']
    reminder = random.choice(reminders)
    text = name5 + " is " + word + " " + description + " hates " + hate + " " + now + " " + reminder
    return text

def generate_comment_5():
    descriptions2 = ['The umpa lumpa', 'The Cheeto', 'The Angry Creamsicle', 'Captain Chaos', 'Orange Julius', 'The Screaming Carrot Demon', 'Trumplethinskin', 'Tiny Hands']
    description2 = random.choice(descriptions2)
    places = ['Iran', 'Mexico', 'North Korea', 'China', 'Afghanistan', 'Syria', 'himself', 'Chrissy Teigen', 'the border wall']
    place = random.choice(places)
    promises = ['breaks promises.', 'cheats on tests.', 'lies.', 'downplays situations.', 'steals.']
    promise = random.choice(promises)
    froms = ['America is', 'Americans are', 'People are', 'You are', 'Your social security is']
    from1 = random.choice(froms)
    dangers = ['in danger', 'in trouble', 'screwed', 'at risk', 'in jeopardy']
    danger = random.choice(dangers)
    text = description2 + " talks more about " + place + " than about America and Americans." + " He " + promise + " "+ from1 + " " + danger + " if he wins. He must lose!"
    return text

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''

    choices = [generate_comment_0, generate_comment_1, generate_comment_2, generate_comment_3, generate_comment_4, generate_comment_5]
    final_comment = random.choice(choices)
    text = final_comment()
    return text
"""
total_comment = 0
for i in range(10000):
    if total_comment == i:
        print (generate_comment())
        total_comment += 1
""" 

# connect to reddit 
reddit = praw.Reddit('bot')

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jn6w93/mitch_mcconnell_just_adjourned_the_senate_until/'
submission = reddit.submission(url=reddit_debate_url)
#comment = reddit.comment(url='https://www.reddit.com/r/csci040/comments/j9vb5b/the_2020_election_bot_debate_thread/g8ms0z0/')

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
#while True: (this makes it a daemon)

while True: 
    try: 
        # printing the current time will help make the output messages more informative
        # since things on reddit vary with time
        print()
        print('new iteration at:',datetime.datetime.now())
        print('submission.title=',submission.title)
        print('submission.url=',submission.url)

        # FIXME (task 0): get a list of all of the comments in the submission
        # HINT: this requires using the .list() and the .replace_more() functions
        all_comments = []
        num_comments = 0
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            all_comments.append(comment)
            num_comments += 1
        print('Total Comments =',len(all_comments))
        
        #print('All Comments per user = ', all_comments) 
        #print('Top Total Comments=', len(submission.comments))
        # HINT: 
        # we need to make sure that our code is working correctly,
        # and you should not move on from one task to the next until you are 100% sure that 
        # the previous task is working;
        # in general, the way to check if a task is working is to print out information 
        # about the results of that task, 
        # and manually inspect that information to ensure it is correct; 
        # in this specific case, you should check the length of the all_comments variable,
        # and manually ensure that the printed length is the same as the length displayed on reddit;
        # if it's not, then there are some comments that you are not correctly identifying,
        # and you need to figure out which comments those are and how to include them.
            #print('len(all_comments)=',len(all_comments))

        # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
        # HINT: 
        # use a for loop to loop over each comment in all_comments,
        # and an if statement to check whether the comment is authored by you or not
        not_my_comments = []
        my_bot = 'botdessert'


        for comment in all_comments:
            if str(comment.author) != 'botdessert':
                not_my_comments.append(comment)
        print('Not My Comments = ',len(not_my_comments))

    #print('All Comments per user = ', all_users) 
        # HINT:
        # checking if this code is working is a bit more complicated than in the previous tasks;
        # reddit does not directly provide the number of comments in a submission
        # that were not gerenated by your bot,
        # but you can still check this number manually by subtracting the number
        # of comments you know you've posted from the number above;
        # you can use comments that you post manually while logged into your bot to know 
        # how many comments there should be. 
        #print('len(not_my_comments)=',len(not_my_comments))

        # if the length of your all_comments and not_my_comments lists are the same,
        # then that means you have not posted any comments in the current submission;
        # (you bot may have posted comments in other submissions);
        # your bot will behave differently depending on whether it's posted a comment or not
        has_not_commented = len(not_my_comments) == len(all_comments)


        if has_not_commented:
            # FIXME (task 2)
            # if you have not made any comment in the thread, then post a top level comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit
            submission.reply(generate_comment())
            #print('completed task 2')

        else:
            # FIXME (task 3): filter the not_my_comments list to also remove comments that 
            # you've already replied to
            # HINT:
            # there are many ways to accomplish this, but my solution uses two nested for loops
            # the outer for loop loops over has_not_comments,
            # and the inner for loop loops over all the replies of the current comment from the outer loop,
            # and then an if statement checks whether the comment is authored by you or not
           
        
            #print('line 230')
            comments_without_replies = []
            for comment in not_my_comments:
                response = False
                #print(comment)
                for reply in comment.replies:
                    #print('      ', reply.author)
                    if str(reply.author) == 'botdessert':
                    #if str(reply.author).lower() == 'botdessert': 
                    #if comment.author.name == 'botdessert':
                        response = True
                        #print('inside the if statement')
                    #if str(comment.author) != 'botdessert':
                        #response = False 
                if response == False:
                    comments_without_replies.append(comment) 
        
                
            # HINT:
            # this is the most difficult of the tasks,
            # and so you will have to be careful to check that this code is in fact working correctly
            print('len(comments_without_replies)=',len(comments_without_replies))

        
        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #random.choice(comments_without_replies())
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
        #Extra Credit task 4: Sorted Comment- reply to most upvoted comments first (1 point) 
            try: 
                new_comment = sorted(comments_without_replies, key=lambda comment: comment.score, reverse=True)
                for comment in new_comment:
                    comment.reply(generate_comment())
                    #print('Comment : ', comment.score)
            except IndexError:
                pass 
                #len(comments_without_replies) == 0
                #print('        len of comment without replies = 0')

        
        #Original task 4 (see extra credit task 4 above)
        """
            try:
                x = random.choice(comments_without_replies)
                random_comment = reddit.comment(id = x)
                print('random comment id =', x) 
                random_comment.reply(generate_comment()) 
                #comment = random.choice(comments_without_replies) 
                #comment.reply(generate_comment()) 
            except IndexError:
                pass
                #len(comments_without_replies) == 0
                print('        len of comment without replies = 0')
        """
        #Extra Credit: Upvote comments with your favorite candiate and downvote comments with least favorite (1 point)  
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
        
        """
        #Extra Credit: Upvote and Downnvote comments and submission based on polarity. (2 points--> actually worth 4 points)
        subreddit = reddit.subreddit('csci040temp')

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

           
        for submission in subreddit.new(limit=None):
            sentence = TextBlob(submission.title.lower())
            if 'biden' in submission.title.lower():
                if sentence.sentiment.polarity > 0:
                    submission.upvote()
                    #print('voting up for + biden submission')
                if sentence.sentiment.polarity < 0: 
                    submission.downvote()
                    #print('voting down for - biden submission')
            if 'trump' in submission.title.lower():
                #print('trump = ', blob.sentiment.polarity)
                if sentence.sentiment.polarity < 0: 
                    submission.upvote()
                    #print('voting up for - trump submission')
                if sentence.sentiment.polarity > 0:
                    submission.downvote()
                    #print('voting down for + trump submission')
        
        

    except praw.exceptions.APIException:
        # this gets run if the try code fails;
        # python will not crash
        print('exception found')

        # python to wait 60 seconds before proceeding
        print('starting to sleep')
        time.sleep(60)
        print('done sleeping')
    
   #comment1 = random.choice(comments_without_replies)

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions

    percent = random.random()
    total_submissions = list(reddit.subreddit('csci040temp').top(time_filter='day'))
    if percent < 0.5:
        submission = reddit.submission(url=reddit_debate_url)
    else:
        chosen_subreddit = random.choice(total_submissions)
        submission = reddit.submission(chosen_subreddit)
        
            