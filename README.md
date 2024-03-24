# url_blender
get urls and organize them from messages

**Note: This only works in Mac OS X and may only be compatible with older versions of OS X (pre-Ventura) until a mechanism to query the new versions is found.**

**Also I only made this to support US-based phone numbers. You can modify the code or message me if you want me to open this up internationally. My e-mail is np327@cornell.edu**

### This script takes all the URLs from a conversation, parses their title, image, and hyperlink and compares their title to a list of keywords/phrases using a plugin that rates their similarity to eachother (the fuzzywuzzy plugin) and sorts them into Word documents categorized as "informational.docx", "entertainment.docx", or "general.docx"

The inspiration for this script came from my own compulsion to send links to myself as messages whenever I found something I was interested by. I needed a way to consume all the links I sent myself, which through this project I found were about 2,500 so far till date. I also wanted to be able to get links from conversations with friends. I figured if I have a need for this then others must have a need as well and decided to make it.

I manually curated the keywords/phrases by grabbing them from the keywords in my ~2,500 links (most of which were YouTube videos, although any link works). You can see them in the url_blender.py script and let me know if you have any suggestions for changes.

## In Case of Error

If you see the message when running the script the first time:

`ls: Messages: Operation not permitted`

Go to System Preferences > Privacy & Security and enable Terminal for Full Disk Access.

![Enable Terminal Full Disk Access](https://cdn.cleanmymac.com/blog_articles/February2023/operation%20not%20permitted%20error4.png)

# Instructions for Use

![Install Python](https://cdn.osxdaily.com/wp-content/uploads/2018/06/install-python3-on-mac.jpg)

The first step is to install the latest stable version of Python 3

As of this writing that is Python 3.12.2

[Download Python](https://www.python.org/downloads/)

Then in Terminal install the following packages using the commands:

`pip3 install validators`

`pip3 install requests`

`pip3 install python-docx`

`pip3 install fuzzywuzzy`

`pip3 install python-Levenshtein`

`pip3 install bs4`

## To Run The Script

Run the command from the directory the 'url_blender.py' script is in:

`python3 url_blender.py`

You'll be prompted with 3 messages:

`What is the username for your account to connect to the database (no spaces please):`

An example input would be johnsmith

`What is the phone number which conversation you're getting your links from? (no dashes, eg. '7775551234')`

An example input would be 3134441234

`Are you getting the links from your own texts (Y) or your friend's/other's (n)?`

An example input would be n

*For the last 2 prompts if you're using this script like I did to get URLs you send to yourself in iMessage, then put in your own number and say Y to the last question because I think it organizes things better. Both ways (Y or n) may work. Try them out to see your output!*

In your Terminal window you will see the following messages print:

`Failed to retrieve the web page. Status code: {response.status_code}`

`An error occurred`

These messages indicate that the URL input did not work so it was not processed (like if a video is deleted or made private or webpage is down).

And then you will see something like:

```
"You know WWE is fake, right?" entertainment
100
WWE
```

**Note: If you find that the processes stop or hang and no new data is being printed to the terminal press Ctrl + C to interrupt and force it to continue. I found this happened to me in one case when trying to grab the links I sent from a conversation.**

The first line is the title of your URL with the category it's placed in at the end of it (entertainment in this case). Then the second line is the fuzzywuzzy score that will have to be greater than 75 and it is the score for comparing the keyword on the third line (WWE) with the title ("You know WWE is fake, right?") for closeness.

The script will keep going unless you interrupt it with Ctrl + F or it runs to completion.

**The output of the script are three Word documents "informational.docx", "entertainment.docx", and "general.docx"**

In these documents will your URLs be organized each with a title, picture, and hyperlink URL.

You can move these files (to save your curated links) or delete them and run the script again (say, for a different conversation) and it will output these files for you again!

Thank you for reviewing my script and hopefully it has come in handy for you.

## Future Feature Implementations

1. Incorporating support for new versions of Mac OS X that are foregoing storing messages in chat.db and instead are encoding them as a hex blob in the attributedBody column. source: https://spin.atomicobject.com/search-imessage-sql/ (under section March 2024 Update)
2. Adding functionality for WhatsApp and enabling you to grab URLs from conversations there to place in Word files
3. Making it possible to make this script work in group texts- as of now I haven't got this working as far as I know
4. Separating the file structure further than "informational", "entertainment", and "general" so things are organized further
5. Allowing for the script to update the Word documents with new URLs from new messages by scanning to see if previous data are there in our documents instead of having to process all the messages again just to get new links added to our Word documents