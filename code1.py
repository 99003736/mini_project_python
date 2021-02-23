import re
p=re.I
def search_string_in_file(file_name, string_to_search,p):
   
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
                return list_of_results
#pattern=re.compile("software",re.I)
matched_lines = search_string_in_file('input_file.txt',"Software",p)
print('Total Matched lines : ', len(matched_lines))
for elem in matched_lines:
    print('Line Number = ', elem[0], ' :: Line = ', elem[1])