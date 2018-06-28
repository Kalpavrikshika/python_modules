class GetTest(object):
    def __init__(self, name):
        print("Greetings!! {}". format(name))
    def another_method(self):
        print("I am another method which is not \n "
                "automatically called")
a = GetTest('Kalpa')
#output: Greetings!!

a.another_method()
#OUtput:I am another methid which is not automatically called