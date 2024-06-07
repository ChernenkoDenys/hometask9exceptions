# Напишіть програму, 
# яка відкриває файл для читання та обробляє помилку FileNotFoundError, якщо файл не знайдено.

filename = "example.txt"
file = None

try:
    file = open(filename, 'r')
except FileNotFoundError as e:
    print(e)
    print("Sorry, cannot find file")
finally:
    if file:
        print("Closing file...")
        file.close()