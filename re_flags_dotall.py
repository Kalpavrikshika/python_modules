import re

text = 'This is some text -- with punctuation.\nA second line'
pattern = r'.+'
no_newlines = re.compile(pattern)
'''Dotall is a flag related to multiline.Dot character matches 
everything in the input text except newline character.'''

#matches anything except a newline character.

dotall = re.compile(pattern, re.DOTALL)

print ('Text:\n   {!r}'.format(text))
print('Pattern:\n  {}'.format(pattern))
print('No newlines :')
for match in no_newlines.findall(text):
    print('   {!r}'.format(match))
print('Dotall   :')
for match in dotall.findall(text):
    print('   {!r}'.format(match))