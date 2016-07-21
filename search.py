# Created by: Harsh Patel
# Automation for searching through command line using python

import requests, webbrowser, sys, bs4

# Argument error/help message
if len(sys.argv) < 3:
    print ('\n' + 'Too few arguments!')
    print ('Make sure to type: python search.py [num of results shown after search] [search query]' + '\n')
    exit()    

# Wait message
print ('\n' + 'Googling...')

# Setting custom num of results
cust = int(sys.argv[1])

# Obtaining the google search's web content
url = 'http://google.com/search?q=' + '+'.join(sys.argv[2:]) 
res = requests.get(url)
res.raise_for_status()

# Using beautiful soup to look at the html content, and obtaining search result links
soup = bs4.BeautifulSoup(res.text, "lxml")
linkElems = soup.select('.r a')

# Determining number of tabs to open
numOpen = min(cust, len(linkElems))

# Simply opening the first google search page for reference
webbrowser.open(url)

# Opening tabs in browser with newest tab being top search result (reverse of search page)
for tab in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[numOpen-tab-1].get('href'))
