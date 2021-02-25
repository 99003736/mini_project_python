import re

input_word=int(input('enter_the_number_of_lines:'))
for i in range(0,input_word):
    count=0
    user_search_input=input("enter the words: ")
    lines=0
    #pattern=re.compile(user_search_input,re.I)
    with open ("input_file.txt","rt")as file_input:
        cc=file_input.read()
        file_input1=re.split('\W+',cc)
        for file_line in range(len(file_input1)):
            lines+=1
            if re.fullmatch(user_search_input,file_input1[file_line],re.M |re.I):
                count+=1
                with open("{}.txt".format(user_search_input),'a') as file_output:
                    file_output.writelines(str(count)+':')
                    file_output.write(file_input1[file_line-1]+" " +file_input1[file_line]+" "+file_input1[file_line+1]+'\n') 

        
        print(count)
            



'''import re
count=0
software=[]
lines=0
pattern=re.compile("software",re.I)

with open ("input_file.txt","rt")as file_input:
    for file_line in file_input:
        lines+=1
        if pattern.search(file_line)!=None:
            software.append((lines,file_line.rstrip('\n')))
    for string in software:
        count+=1
        with open("software.txt",'a') as file_output:
            file_output.writelines(str(count)+':')
            file_output.writelines(string[1]+'\n') '''