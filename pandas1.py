import pandas as pandas

'''let’s tell Pandas that row 0 of the table has column headers and 
ask it to convert text-based dates into time objects:'''

calls_df, = pandas.read_html("http://apps.sandiego.gov/sdfiredispath/", header=0, parse_dates=["Call Date"])
print(calls_df)