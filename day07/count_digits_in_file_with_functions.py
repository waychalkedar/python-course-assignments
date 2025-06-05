import sys
import file_read as fr 

try:
    file = sys.argv[1]
except Exception as err:
    print("No file provided.")
    exit()

numbers_as_string = fr.file_as_string(file)
combined_string = (numbers_as_string.replace("\n", "")).replace(" ", "")

write_file = r".\report.txt"
with open(write_file, "w") as fh_write:
    for num in range(10):
        fh_write.write(f"{num} {combined_string.count(str(num))} \n")


