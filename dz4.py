def convert_to_number(input_string):
    if '.' in input_string or 'e' in input_string or 'E' in input_string:
        return float(input_string)
    else:
        return int(input_string)

def main():
    input_string = input("Введіть рядок, який потрібно перетворити на число: ")
    
    try:
        result = convert_to_number(input_string)

        print(f"Перетворене число: {result}")
    
    except ValueError:
        print("Помилка: Невірний формат числа.")

if __name__ == "__main__":
    main()








def convert_to_number(input_string):
    try:
        if '.' in input_string or 'e' in input_string or 'E' in input_string:
            return float(input_string)
        else:
            return int(input_string)
    except ValueError:
        print("Помилка: Невірний формат числа.")
        return None

def main():
    input_string = input("Введіть рядок, який потрібно перетворити на число: ")

    result = convert_to_number(input_string)

    if result is not None:
        print(f"Перетворене число: {result}")

if __name__ == "__main__":
    main()
