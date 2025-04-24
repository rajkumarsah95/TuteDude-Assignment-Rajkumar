try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line, end="")  # end="" prevents print from adding an extra newline
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")