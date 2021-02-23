user_search_value = input("Enter the value or string to search for: ")

count = 0    

with open('input_file.txt', 'r+') as f:
    for line in f.readlines():
        words = line.lower().split()
        for word in words:
            if word == user_search_value:
                count += 1
print (count)

