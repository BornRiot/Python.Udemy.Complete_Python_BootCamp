"""
Code pertains to the topic of web scraping and covers the video lecture
in corresponding section of the course.
"""


# These are the steps that can be taken when grabbing a title from a website
# using web scraping
# Step 1: import requests and create a variable for the requests link
import requests
result = requests.get('https://example.com/')

#Step 2: Find what variable type is result
print(type(result))

#Step 3: Get the text format of the html doc for example.com
print(result.text)


# Step 4: Parse through html doc using beautiful soup
import bs4
soup = bs4.BeautifulSoup(result.text,'lxml')
print("Below is the output of the soup object:")
print(soup)

# Step 5: Select element from html doc using select from beautiful soup
get_title = soup.select('title')
print(get_title)

# Step 6: return only the title of the site without tags
print(get_title[0].getText())

# Step 7: grab all the paragraph elements in the html doc.
site_paragraphs = soup.select('p')
print(site_paragraphs[0].getText())
# print var type
print(type(site_paragraphs))
