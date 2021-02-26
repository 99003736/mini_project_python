'''*********************************************************************
Author=Ajit A bijapur
Date:-26/02/2021
PS no:-99003736
contact email id:-ajit.bijapur@ltts.com
File Description :finding the words in the given
                 input find and store those words in the output file
                 also printing the number of time that word as occurred
***************************************************************************'''
import re  # import regular expression


class text_processing:  # creating the class of text_processing
    def __init__(self, file_name):  # creating the constructor
        self.file_name = file_name


class find(text_processing):  # calling parent class in the child class
    def search(self):
        # enter the number of words u need to search
        search = int(input('enter the :'))
        # loop for number of words u need to search
        for i in range(0, search):
            count = 0
            # enter the word you need to search
            user_search_input = input("enter the words: ")
            lines = 0
            # reading the input files
            with open("input_file.txt", "rt")as file_input:
                File = file_input.read()
                # spliting the whole file_input into list
                file_input1 = re.split('\W+', File)
                for file_line in range(len(file_input1)):
                    lines += 1
                    # find the word through the re.match regular expression
                    if re.fullmatch(user_search_input, file_input1[file_line],
                                    re.M | re.I):
                        count += 1
                        with open("{}.txt".format(user_search_input),
                                  'a') as file_output:
                            file_output.writelines(str(count)+':')
                            #  to get the preceding and succeeding word
                            file_output.write(file_input1[file_line-1] + " " +
                                              file_input1[file_line] + " " +
                                              file_input1[file_line+1] +
                                              '\n')
                print(count)
filename = 'input_file.txt'

b = find(filename)   # creating object
b.search()         # calling the class through object and accesing the function