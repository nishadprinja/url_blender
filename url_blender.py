import sqlite3
import validators
import requests
from bs4 import BeautifulSoup
from validators import ValidationFailure

def is_string_a_url(url_string):
    result = validators.url(url_string)

    if isinstance(result, ValidationFailure):
        return False

    return result

# Create a SQL connection to our SQLite database
con = sqlite3.connect("/Users/nishadprinja/Library/Messages/chat.db")

cur = con.cursor()
rows = cur.execute('SELECT datetime (message.date / 1000000000 + strftime ("%s", "2001-01-01"), "unixepoch", "localtime") AS message_date, message.text, message.is_from_me, chat.chat_identifier FROM chat JOIN chat_message_join ON chat. "ROWID" = chat_message_join.chat_id JOIN message ON chat_message_join.message_id = message. "ROWID" WHERE chat_identifier = "+18457097580" AND is_from_me = "0"')

# The result of a "cursor.execute" can be iterated over by row

rowz = rows.fetchmany(50)

for row in rowz:
    if is_string_a_url(row[1]):

        try:
            # Step 1: Fetch the web page
            url = row[1]
            response = requests.get(url)

            if response.status_code == 200:
                # Step 2: Parse the HTML content
                soup = BeautifulSoup(response.text, 'html.parser')

                # Step 3: Extract metadata
                title = soup.find("meta", property="og:title")
                image = soup.find("meta", property="og:image")
                tag = soup.find("meta", property="og:video:tag")

                print(url)
                print(title["content"] if title else "No meta title given")
                print(image["content"] if image else "No meta image given")
                print(tag["content"] if tag else "No meta tag given")
                print("\n")
                
            else:
                print("Failed to retrieve the web page. Status code: {response.status_code}")
            
        except:
            print("An error occurred")


# Be sure to close the connection
con.close()