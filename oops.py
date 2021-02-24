class test:
    def __init__(self,input1=1,input2=2):
        print("1st class")
    def myfunc(self):
        self.input1=input1
        self.input2=input2
        return input1*input2      
           
myobj=test()
a=myobj.myfunc
print(a)


        