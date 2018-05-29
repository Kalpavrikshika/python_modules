class Parentheses:
    def check(self, input):
        self.input = input
        if '(' in input and ')' not in input:
            print ('error-missing )')
        if ')' in input and '(' not in input:
            print ('error-missing (')
        if '{' in input and '}' not in input:
            print ('error-missing }')
        if '}' in input and '{' not in input:
            print ('error-missing }')
        if '[' in input and ']' not in input or ']' in input and '[' not in input:
            print ('error-missing ]')
        if ']' in input and '[' not in input:
            print ('error-missing [')
        else:
            print('ok')
valid=Parentheses()
valid.check('{this, (), ]')