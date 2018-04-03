from re_testpattern import test_patterns

test_patterns('abbaabbba',
[
    ( '[ab]', "either a or b"),
      ('a[ab]*' , "a followed by zero or more a or b"),
      ('a[ab]+', "a followed by one of more a or b"),
      ('a[ab]+?', "a followed by one or more a or b, greedless")],
)
