filename = input("Enter a filename: ")

with open(filename,'r', encoding='utf-8') as file:
    print(file.read())
