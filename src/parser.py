 FILE = '../data/reut2-000.sgm'

from bs4 import BeautifulSoup
soup = BeautifulSoup(open(FILE), "html.parser") # consider using lxml to get better speed
entries = soup.find_all('reuters') # get entries
dates = soup.find_all('date') # get entries
titles = soup.find_all('title') # get entries
topics = soup.find_all('topics') # get entries
datelines = soup.find_all('dateline') # get entries
reuters = soup.find_all("reuters", attrs={"oldid":"16309"})

print('stop')

