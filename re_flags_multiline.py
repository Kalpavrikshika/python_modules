import re

text = 'This is some text -- with punctuation.\nA second line.'
pattern = r'(^\w+) | (\w+\S*$)'
single_line = re.compile(pattern)
'''multiline flag controls how the pattern matching code processes anchoring
instructions for text containing new line characters'''
multiline = re.compile(pattern, re.MULTILINE)

print('Text:\n  {!r}'.format(text))
print('Pattern:\n  {}'.format(pattern))
print('Single Line :')

for match in single_line.findall(text):
    print ('  {!r}'.format(match))
print('Multiline   :')
for match in multiline.findall(text):
    print('   {!r}'.format(match))

