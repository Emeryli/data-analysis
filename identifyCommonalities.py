# Create an empty dictionary
kvDic = {}
flag = True

while flag:
    # Use try except block to handle unexpected inputs from users
    try:
        # Read a text file
        file_name = input("Enter FULL file name: ")
        with open (file_name, 'r') as file:
            copied_data = file.read()
            
    # if unsuccessful, skip the rest of the code in the current block and enter a new loop
    except Exception as e:
            print(f"{e}\nPlease try again")
            continue
        
    # Clean up data
    column = copied_data.split('\n')
    column = [item.strip() for item in column if item.strip() !='' and item]
    
    # Add column into kvDic
    columnName = column[0]
    for i in range(1, len(column)):
        key = column[i]
        if key not in kvDic:
            kvDic[key] = [columnName]
        else:
            kvDic[key].append(columnName)
            
    # Ask user if they want to continue adding or not
    indicator = input("Do you want to continue adding? (Y/N): ")
    if indicator =="N":
        break

# Sort the dictionary based on the number of values in each key
sorted_data = dict(sorted(kvDic.items(), key=lambda item: len(item[1]), reverse=True))

# Write the result into a text file
file_path = 'output.txt'
with open(file_path, 'w') as file:
    for key, values in sorted_data.items():
        file.write(f"{key}\n")
        for value in values:
            file.write(f"  - {value}\n")
        file.write("\n")
print(f"Data successfully written to {file_path}")

