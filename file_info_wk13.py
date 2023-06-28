import os

dict_list = []  # Initialize an empty list to store dictionaries

for file in os.listdir():  # Iterate over the files in the current directory
    file_dict = {}  # Create an empty dictionary for each file
    
    file_dict['path'] = os.path.realpath(file)  # Store the real path of the file in the dictionary
    file_dict['size'] = os.path.getsize(file)  # Store the size of the file in the dictionary
    
    dict_list.append(file_dict)  # Add the dictionary to the list
    
print(*dict_list, sep="\n")  # Print each dictionary in the list on a new line
