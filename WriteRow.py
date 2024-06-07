# Створіть функцію, яка приймає рядок від користувача та записує його у файл.

filename = "writerow.txt"
file = None

def write_into_file(string_to_check: str):
    string_to_write = string_to_check + "\n"
    try:
        file = open(filename, "a")
    except FileNotFoundError as e:
        print(e)
        print(f"File {filename} not existing")
    
    if file is not None:
        file.write(string_to_write)
        file.close()    
    


def main():
    input_string = input("Enter ur string: ")
    write_into_file(input_string)


if __name__ == "__main__":
    main()