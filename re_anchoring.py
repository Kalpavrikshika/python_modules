from re_testpattern import test_patterns

test_patterns('This is some text -- with punctuation.',
[
#^ anchors 'start of string, or line'
(r'^\w+', 'word at start of the string'),
#\A anchors 'start of string'
(r'\A\w+', 'word at start of string'),
#\w - alphanumeric \S - non-whitespace $ - end of string or line
(r'\w+\S*$', 'word near the endd of the string'),
(r'\w+\S*\Z', 'word near end of the string'),
(r'\w*t\w*', 'word containing t'),
#\b- empty string at the beginning or end of a word
(r'\bt\w+', 't at start of word'),
#\w+t gives "text" in output, and \wt gives "xt" in output
(r'\w+t\b', 't at end of the word'),
(r'\Bt\B', 't, not start or end of word')],
)