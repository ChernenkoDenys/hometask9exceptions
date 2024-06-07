# Напишіть програму, яка читає вміст текстового файлу та виводить кількість слів у ньому.

filename = "Wordsinfilecount.txt"
file = None

words_count = 0

try:
    file = open(filename, 'r')
    for line in file:
        words_list = line.split()
        for word in words_list:
            words_count += 1
except FileNotFoundError as e:
    print(f"File {filename} is not existing")
finally:
    if file is not None:
        file.close()
    
print(f"Words count in file: '{filename}' is '{words_count}'")


        
