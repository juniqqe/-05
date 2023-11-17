def check_strings(strings):
    for i in range(1, len(strings)):
        current_length = len(strings[i])
        previous_length = len(strings[i - 1])

        if current_length % previous_length == 0:
            return "Ура!"

    return "Увы!"

def main():
    try:
        # Ввод количества строк
        n = int(input("Введите количество строк (минимум 2): "))
        
        if n < 2:
            print("Количество строк должно быть как минимум 2.")
            return

        # Ввод самих строк
        strings = []
        for i in range(n):
            string = input(f"Введите строку {i + 1}: ")
            strings.append(string)

        result = check_strings(strings)
        print(result)

    except ValueError:
        print("Ошибка: Введите корректное число.")

if __name__ == "__main__":
    main()
    