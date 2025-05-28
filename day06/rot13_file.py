import sys

filename = sys.argv[1]

def main():
    try:
        with open(filename, "r") as fh:
            converted = rot13(fh.read()) 
    except Exception as err:
        print(f"Trouble with '{filename}'. Error: {err} ")
        exit()

    with open(filename, "w") as file_write:
        file_write.write(converted)

def rot13(filecontents):
    converted_contents = ""
    for ch in filecontents:
        if 65 <= ord(ch) <= 90: # test for capital letters
            ch = chr(ord(ch) + 13)
            if ord(ch) > 90:
                ch = chr(ord(ch) - 26)
        elif 97 <= ord(ch) <= 122: # test for small letters
            ch = chr(ord(ch) + 13)
            if ord(ch) > 122:
                ch = chr(ord(ch) - 26)
        else: # not an alphabet
            converted_contents = converted_contents + ch
            continue
        converted_contents = converted_contents + ch
    return converted_contents

main()