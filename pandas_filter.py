import pandas as pandas
#filter pandas results.
calls_df, = pandas.read_html("http://apps.sandiego.gov/sdfiredispatch/", header=0, parse_dates=["Call Dates"])
calls_df.describe()
calls_df.groupby("Call Type").count()
calls_df["Unit"].unique()