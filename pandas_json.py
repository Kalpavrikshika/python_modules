import pandas as pandas

calls_df, = pandas.read_html("http://apps.sandiego.gov/sdfireddispath/", header=0, parse_dates=["Call Dates"])
print(calls_df.to_json(orient="records", date_format="iso"))