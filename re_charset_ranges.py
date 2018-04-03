from re_testpattern import test_patterns

test_patterns(
    'This is some text -- with punctuation.',
    [
        ('[a-z]+', 'sequences of lower case'),
        ('[A-Z]+', 'sequences of upper letters'),
        ('[a-zA-Z]+', 'sequences of letters of either case'),
        ('[A-Z][a-z]+', 'one uppercase followed by lowercase'),
    ]
)