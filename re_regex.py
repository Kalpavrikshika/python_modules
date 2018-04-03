import re
regexes = [
    re.compile(p) 
    for p in ['this', 'that']
]
text = "Does this text match the pattern"

print("text {!r}\n".format(text))

for regex in regexes:
    print ('seeking "{}" -> '.format(regex.pattern), end = ' ')

    if regex.search(text):
        print ("match")

    else:
        print("No match")