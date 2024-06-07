# Реалізуйте програму, яка копіює вміст одного файлу в інший.

from_file_copy = "copyfile1.txt"
to_file_copy = "copyfile2.txt"

file1 = None
file2 = None

try:
    file1 = open(from_file_copy, 'r')
except FileNotFoundError as e:
    print(e)
    print(f"File {from_file_copy} not existing")

try:
    file2 = open(to_file_copy, 'w')
except FileNotFoundError as e:
    print(e)
    print(f"File {to_file_copy} not existing")
    
if file1 is not None or file2 is not None:
    for line in file1:
        file2.write(line)
    
if file1 is not None:
    file1.close()

if file2 is not None:
    file2.close()