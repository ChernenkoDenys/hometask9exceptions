# Створіть програму, яка отримує від користувача два інпути,
# конвертує цей інпут до числа і відловлює помилку, якщо конвертувати не вийшло.

num_1_input = input("Enter your first number: ")
num_2_input = input("Enter your second number: ")

try:
    num_1 = int(num_1_input)
except ValueError:
    print(f"Failed to convert the first number: {num_1_input}")
    num_1 = None

try:
    num_2 = int(num_2_input)
except ValueError:
    print(f"Failed to convert the second number: {num_2_input}")
    num_2 = None

print("First number:", num_1)
print("Second number:", num_2)