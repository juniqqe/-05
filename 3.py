def main():
    numbers = []  # Список для хранения введенных чисел

    # Ввод чисел от пользователя до появления первого нуля
    while True:
        num = int(input("Введите целое число (0 для завершения): "))
        
        if num == 0:
            break  # Прерываем цикл при вводе 0
        elif abs(num) <= 1000:
            numbers.append(num)  # Добавляем число в список

    # Проверяем, что введены хотя бы два ненулевых числа
    if len(numbers) >= 2:
        # Выводим минимальное и максимальное ненулевые числа
        print("Минимальное число:", min(numbers))
        print("Максимальное число:", max(numbers))
    else:
        print("Недостаточно чисел для вычисления минимального и максимального.")

if __name__ == "__main__":
    main()