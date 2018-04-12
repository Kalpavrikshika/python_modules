import re
import urllib.request
import operator

#download wiki page
url = "https://en.wikipedia.org/wiki/Diplomatic_history_of_World_War_II"
html = urllib.request.urlopen(url).read()

#find all mentioned years in the 20th or 21st century.
regex = r'\b(?:19|20)\d{2}\b'
matches = re.findall(regex, str(html))

#form a dict of the number of occurences of each year
year_counts = dict((year, matches.count(year)) for year in set(matches))

#print the dict sorted in descending order
for year in sorted(year_counts, key=year_counts.get, reverse=True):
    print(year, year_counts[year])