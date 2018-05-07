import pandas as pandas
#the pandass library has a built-in method to scrape tabular data from html pages.
#with function read_html()
tables = pandas.read_html("https://apps.sandiego.gov/dsfiredispatch/")
print(tables[0])