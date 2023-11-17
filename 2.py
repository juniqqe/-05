def calculate_growth(start_height, years, moisture):
    current_height = start_height
    min_height = max_height = start_height
    
    for year in range(1, years + 1):
        growth_rate = 0

        if 12 <= moisture <= 16:
            growth_rate = 0.05
        elif 3 <= moisture < 12:
            growth_rate = -0.05
        elif 16 < moisture <= 26:
            growth_rate = 0.03
        
        current_height *= (1 + growth_rate)
        min_height = min(min_height, current_height)
        max_height = max(max_height, current_height)
        
        print(f"Year {year}: Height - {current_height:.2f} cm, Growth - {(current_height - start_height):.2f} cm")
        
        if moisture == 0:
            break
    
    return min_height, max_height

start_height = 4  # Начальная высота дерева
years = 7  # Количество лет

while True:
    moisture = int(input("Введите влажность почвы (0 для завершения): "))
    
    if moisture == 0:
        break
    
    min_result, max_result = calculate_growth(start_height, years, moisture)
    print(f"Минимальная высота: {min_result:.2f} см")
    print(f"Максимальная высота: {max_result:.2f} см")
    