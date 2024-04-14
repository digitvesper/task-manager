class Store:
    def __init__(self, name, address, assortment):
        self.name = name
        self.address = address
        self.assortment = assortment

    def display_info(self):
        print(f"Магазин: {self.name}")
        print(f"Адрес: {self.address}")
        print("Ассортимент товаров:")
        for item in self.assortment:
            print(f"- {item}")

# Пример использования класса Store

# Создание магазина
store1 = Store("Магазин одежды", "ул. Ленина, 123", ["Футболки", "Джинсы", "Платья"])
store2 = Store("Магазин техники", "пр. Победы, 45", ["Смартфоны", "Ноутбуки", "Телевизоры"])

# Вывод информации о магазинах
store1.display_info()
print()
store2.display_info()