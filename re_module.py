import re


pattern = "this"
text = "Does this text have a pattern"

match = re.search(pattern, text)

s= match.start()
e = match.end()

print('Found "{}" in "{}" from {} to {}, {}'.format(match.re.pattern, match.string, s, e, text[s:e]))