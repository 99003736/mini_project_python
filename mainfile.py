''''user_search_value = input("Enter the value or string to search for: ")

count = 0    

with open('input_file.txt', 'r+') as f:
    for line in f.readlines():
        words = line.lower().split()
        for word in words:
            if word == user_search_value:
                count += 1
print (count)'''

import re

class text_processing:
    

    def __init__(self,file_name):
        self.file_name = file_name
      
        
        
    def search(self):
        input_word=int(input('enter_the_number_of_words:'))
        for i in range(0,input_word):
            count=0
            self.search_pat = input("enter the words: ") 
            output=[]
            lines=0
            
            pattern=re.compile(self.search_pat,re.I|re.M)   
            with open (self.file_name,"rt")as file_input:
               
                #print(re.split('\W+',str(file_input)))
                for file_line in file_input:
                    lines+=1

                    if pattern.search(file_line)!=None:
                        output.append((lines,file_line.rstrip('\n')))
                for string in output:
                    count+=1
                    with open("{}.txt".format(self.search_pat),'a') as file_output:
                        file_output.writelines(str(count)+':')
                        file_output.writelines(string[1]+'\n') 
        print(count)
           
#  print('Word = ', elem[0], ' :: Line Number = ', elem[1], ' :: Line = ', elem[2])

       
           
def main():
    filename = 'input_file.txt'
    x = text_processing(filename)
    x.search()

main()
