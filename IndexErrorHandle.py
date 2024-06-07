# Обробіть виняток IndexError, коли програма 
# намагається отримати доступ до неправильного індексу в списку.

list_with_words = ['apple', 'banana']

try:
    index_number = int(input("Enter ur number to access list: "))
    print(list_with_words[index_number])
except ValueError as e:
    print(e)
    print(f"Error index must be a number")
except IndexError as e:
    print(e)
    print("Error cannot access element with this index in the list")
finally:
    print("End of Work")