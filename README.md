# reddit-vibe-checker

A python script to check if the vibe of a subreddit is positive, negetive or netural. This script makes the use of NLTK which is capable of doing tokenization of sentences and as a result it is able to identify the tone of it. The accuracy in identifying the tone majorly depends on NLTK.


What this scipt does:
- Gives overall vibe.
- Top three most positive posts.
- Top three most negetive posts.

![Screenshot-reddit-vibe-checker](https://github.com/user-attachments/assets/e23f8eee-0f86-419c-8ce8-a2ebb6fbb3be)


## Usage guide

## Step 1 - Install these python packages if not already:
- praw
- pandas
- matplotlib
- nltk

## Step 2 - You must create reddit ID
In the first part of the script you will find client_id=, client_secret=, user_agent= (These details must be filled by you, follow allong to know how). These details are requried by praw to visit reddit and download posts and subreddit data. You can easily find these details just follow this link:

[https://www.geeksforgeeks.org/how-to-get-client_id-and-client_secret-for-python-reddit-api-registration/]

remember user_agent will be the name you will put to create the app.

## Step 3 - Add subreddit name
Change cats to any subreddit you want to study in this line:

`subreddit_name = "cats"`

additionally, you can change the total number of posts which this script can download from this line:

`posts_required = 100`


## Step 4 - Done!
Once the above steps are done you are ready to go. If you are new then make sure the scipt is executable, in linux you can do `chmod +x scriptname.py` to make it executable.



