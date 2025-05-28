import sys

try:
    filename = sys.argv[1]
except Exception as err:
    print("No file provided.")
    exit()

try:
    with open(filename, "r") as fh:
        numbers_as_string = fh.read()
except Exception as err:
    print(f"Trouble with '{filename}'. Error: {err} ")
    exit()

combined_string = (numbers_as_string.replace("\n", "")).replace(" ", "")

write_file = r".\report.txt"
with open(write_file, "w") as fh_write:
    for num in range(10):
        fh_write.write(f"{num} {combined_string.count(str(num))} \n")


