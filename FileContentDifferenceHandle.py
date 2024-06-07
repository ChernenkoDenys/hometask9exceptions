# Напишіть програму, яка відкриває два файли для читання та порівнює їх вміст, 
# виводячи рядки, які є у першому файлі, але відсутні у другому.

first_filename = "filecontent1.txt"
second_filename = "filecontent2.txt"

file1 = None
file2 = None

try:
    file1 = open(first_filename, 'r')
except FileNotFoundError as e:
    print(e)
    print("File {first_filename} not existing") 


try:
    file2 = open(first_filename, 'r')
except FileNotFoundError as e:
    print(e)
    print("File {second_filename} not existing") 
    
    
if file1 != None or file2 != None:
    for line in file1.readlines():
        if line not in file2.readlines():
             print(line, end="")
         
file1.close()
file2.close()