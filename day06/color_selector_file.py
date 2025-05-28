import sys

try:
    color_file = sys.argv[1]
    try:
        with open(color_file, "r") as file_read:
            colors_list = file_read.read().splitlines()
        print(f"File selected was {color_file}.")
        for index, color in enumerate(colors_list):
            print(f"{index + 1} {color}")
    except Exception as err:
        print(f"Error: {err} ")
        exit()

except IndexError:
    print("""
      No file was provided.
      The following default colors are available for selection:
      1\tblue
      2\tgreen
      3\tyellow
      4\twhite 
      """)
    colors_list = ['blue', 'green', 'yellow', 'white']
    
col = input("Enter your desired color or the number for it: ")

while(True):
    if col.lower() in colors_list:
        print(f"Chosen color was {col.lower()}")
        break
    
    try:
        num = int(col)
    except ValueError:
        if len(list(col)) > 1:
            col = input("Desired color not in list. Try again: ")
            continue
        col = input("Please enter an integer number: ")
        continue
    
    if num < 1 or num > len(colors_list):
        col = input(f"Please enter an integer number between 1 to {len(colors_list)}: ")
        continue

    print(f"Chosen color was {colors_list[num - 1]}")
    break