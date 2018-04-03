import re

text = "abbbbaaaababa"
pattern= "ab"

for x in re.findall(pattern, text):
    print ("{!r}".format(x))