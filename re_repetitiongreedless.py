#when processing a repetition instruction, re will consume as much of the input as possible.
#This may result in fewer indivisual matches or output of more of the input text than intendded. 
from re_testpattern import test_patterns

test_patterns(
    'abbaabbba',
    [
        ('ab*?', "a followed by zero or more b"),
        ('ab+?', "a followed by one or more b"),
        ('ab??', "a followed by zero or one b"),
        ('ab{3}?', "a followed by 3 b"),
        ('ab{2,3}?', "a followed by 2 to 3 b")
    ]
)