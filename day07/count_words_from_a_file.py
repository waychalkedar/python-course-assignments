import sys

try:
    words_file = sys.argv[1]
    try:
        with open(words_file, "r") as file_read:
            words_string = file_read.read()
    except Exception as err:
        print(f"Error: {err} ")
        exit()
except Exception as err:
    print(f"Error in file input: {err}")
    exit()

words_list = words_string.lower().split()

sorted_words_list = sorted(list(set(words_list)))

write_file = r".\words_and_spaces_counted.txt"

with open(write_file, "w") as file_write:
    for word in sorted_words_list:
        file_write.write(f"{word:<15}{words_list.count(word):>4}\n")