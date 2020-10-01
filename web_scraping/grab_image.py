"""
Module code demonstrates how to use web scraping to grab images from a website
using beautiful soup. Module corresponds to lecture under similar title for the
course.
"""

import requests
import bs4
res = requests.get('https://bit.ly/3mTHCbJ')

soup = bs4.BeautifulSoup(res.text,'lxml')

# Grab first image tag
print(soup.select('img')[0])

# Get images with the class title 'thumpimage'
print(soup.select('.thumbimage'))

# Assign both images to corresponding variables
computer = soup.select('.thumbimage')[0]
print(computer)

# Treat the element as a dictionary because ot is
# a specialized tag object
print('Below is the info on what type of object computer is:')
print(type(computer))
# Call a particalur part of computer dictionary object
print(computer['class'])

# grab computer dictionary key 'src' and paste in a jupyter
# notebook
print(computer['src'])

# Make a request  specifically for the computer image
comp_request = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

# print raw content of image file
print(comp_request.content )

# Save  computer image to local directory using link
# and open()
f = open('the_comp_image.jpg', mode='wb')
f.write(comp_request.content)
f.close()


# To save and open an html document with utf-8 parameters
# with open('C:\DevEx\IdeaProjects\Python.Udemy.Complete_Python_BootCamp\web_scraping\DeepBlue.html', "r", encoding="utf-8") as f:
#     print(f.read().encode('utf-8'))
