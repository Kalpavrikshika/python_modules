import pandas as pandas


calls_df, = pandas.read_html("http://apps.sandiego.gov/sdfiredispatch/", header=0, parse_dates=["Call Dates"])
calls_df.to_csv("calls.csv", index=False")