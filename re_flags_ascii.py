import re

text = u'Français złoty Österreich'
pattern = r'\w+'
#Give Ascii flag to compile in ascii.
ascii_pattern = re.compile(pattern, re.ASCII)
#Defined in unicode by default.
unicode_pattern = re.compile(pattern)

print ('Text   :', text)
print ('Pattern   :', pattern)
print ('ASCII   : ', list(ascii_pattern.findall(text)))
print('Unicode :', list(unicode_pattern.findall(text)))