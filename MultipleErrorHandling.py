# Напишіть програму, яка пропонує користувачу ввести список чисел, відокремлених комами. 
# Перетворіть введений рядок у список цілих чисел і обробляйте помилки 
# ValueError (у випадку невірного введення цілих чисел) 
# та IndexError (у випадку доступу до індексів, що виходять за межі діапазону).


string_with_numbers = input("Enter string with numbers (separated by comma): ")
list_with_numbers = string_with_numbers.split(",")
list_with_integers = []

try:
    for num in list_with_numbers:
        list_with_integers.append(int(num))
    
    print(f"Your list with numbers: {list_with_integers}")
    
    index = int(input("Enter Index to Print the element: "))
    print(list_with_integers[index])
except ValueError as e:
    print("Elements in list and Index must be only integers")
except IndexError as e:
    print("Cannot access element at index")
finally:
    print("Work done")