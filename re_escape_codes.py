from re_testpattern import test_patterns

test_patterns(
    'A prime #1 example!',
    [(r'\d+', 'sequence of digits'),
    (r'\D+', 'sequences of non-digits'),
    (r'\s+', 'sequences of white spaces'),
    (r'\S+', 'sequences of non-white spaces'),
    (r'\w+', 'alphanumeric characters'),
    (r'\W+', 'non-alphanumeric characters')],
)