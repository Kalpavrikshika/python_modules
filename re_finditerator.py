import re

text = "Thisislalala"
pattern = "is"

for x in re.finditer(pattern, text ):
    s = x.start()
    e = x.end()

    print ("found {!r} at {:d} : {:d}".format(text[s:e], s, e))