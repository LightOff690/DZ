def calculate_total_price(weight_grams, price_per_kg):
    # Преобразуем вес из граммов в килограммы
    weight_kg = weight_grams / 1000.0
    
    # Вычисляем итоговую цену
    total_price = weight_kg * price_per_kg
    
    return total_price

# Пример использования функции
weight_grams = 750  # Вес в граммах
price_per_kg = 10.5  # Цена за килограмм
total_price = calculate_total_price(weight_grams, price_per_kg)
print(f"Итоговая цена продукта: {total_price} рублей")