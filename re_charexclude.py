from re_testpattern import test_patterns

test_patterns("This is some text -- with punctuation.",[('[^-. ]+','sequences without -, ., or space ')],
)
