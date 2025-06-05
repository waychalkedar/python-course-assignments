def file_as_string(filename):
    try:
        with open(filename, "r") as fh:
            file_as_string = fh.read()
            return(file_as_string)
    except Exception as err:
        print(f"Trouble with '{filename}'. Error: {err} ")
        exit()