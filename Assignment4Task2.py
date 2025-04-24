l=input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(l)
print("Data successfully written to output.txt.")

a=input("Enter additional text to append : ")
with open("output.txt", "a") as file:
    file.write(a)
print("Data successfully appended.")

print("Final Contents of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line)


