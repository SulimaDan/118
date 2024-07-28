def convert_to_number(input_string):
    try:
        number = int(input_string)
    except ValueError:
        try:
            number = float(input_string)
        except ValueError:
            print("Помилка: Невірний формат числа.")
            return None
    return number

def main():
    input_string = input("Введіть рядок, який потрібно перетворити на число: ")
    
    result = convert_to_number(input_string)

    if result is not None:
        print(f"Перетворене число: {result}")

if __name__ == "__main__":
    main()
