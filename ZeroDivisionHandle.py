# Реалізуйте функцію, яка ділить два числа, але обробляє помилку ZeroDivisionError, 
# якщо друге число дорівнює нулю.
num1, num2 = 3, 1

try:
    result = num1 / num2 
except ZeroDivisionError as e:
    print(e)
    print("U cannot divide by zero! Default Answer: '0'")
    result = 0
finally:
    print(f"Your result is: {result}")