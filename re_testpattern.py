import re

def test_patterns(text, patterns):

    for pattern, desc in patterns:
        print("'{}'({})\n".format(pattern,desc))
        print ("   '{}'".format(text))

        for x in re.finditer(pattern, text):
            s = x.start()
            e = x.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print("   {}'{}'".format(prefix, substr))
        
        print()

    return

#Another way of calling function.
'''if __name__ == '__main__':
    test_patterns("abbaaabbbbaaaaa", 
                    [('ab', "'a' followed by 'b'"),
                    ])'''
test_patterns("abbaaabbbbaaaaa", 
                    [('ab', "'a' followed by 'b'"),
                    ])

