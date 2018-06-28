class GetTest(object):
    def __init__(self):
        self.info = {
            'name' : 'yasoob',
            'Country': 'Pakistan',
            'number' : 12345812
        }
    def __getitem__(self, i):
        return self.info[i]
foo = GetTest()
print (foo['name'])
print (foo['number'])