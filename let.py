user_input = input("enter the text to write in the file:")

with open("output.txt", "w") as f:
    f.write(user_input + "\n")
print("Data successfully written to the output.txt")


more_input = input("enter moredata to append in the file:")

with open("output.txt", "a") as f:
    f.write(more_input + "\n")
print("Data successfully appended")


print("\n final content of output.txt:")
with open("output.txt", "r") as f:
    for line in f:
        print(line.strip())

