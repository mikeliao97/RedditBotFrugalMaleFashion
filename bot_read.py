import praw

user_agent = ("PyEng 0.1")

r = praw.Reddit(user_agent = user_agent)
subreddit = r.get_subreddit("frugalmalefashion")
for submission in subreddit.get_hot(limit = 10):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------")


