class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        return self.items.get(item_name)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def display_items(self):
        print(f"Магазин: {self.name}")
        print(f"Адрес: {self.address}")
        print("Ассортимент товаров:")
        for item, price in self.items.items():
            print(f"{item}: {price}")

# Создаем несколько объектов класса Store
store1 = Store("Продуктовый магазин", "ул. Ленина, 123")
store2 = Store("Магазин одежды", "пр. Победы, 45")
store3 = Store("Магазин бытовой техники", "ул. Советская, 56")

# Добавляем товары в магазины
store1.add_item("Яблоки", 0.5)
store1.add_item("Бананы", 0.75)
store1.add_item("Молоко", 1.2)

store2.add_item("Футболка", 15.99)
store2.add_item("Джинсы", 29.99)
store2.add_item("Куртка", 49.99)

store3.add_item("Холодильник", 599.99)
store3.add_item("Стиральная машина", 399.99)
store3.add_item("Телевизор", 499.99)

# Тестируем методы магазина
print("Магазин до обновления цены:")
store2.display_items()

store2.update_item_price("Футболка", 12.99)

print("\nМагазин после обновления цены:")
store2.display_items()

print("\nЦена за бананы в магазине 1:", store1.get_item_price("Бананы"))

store1.remove_item("Бананы")
print("\nМагазин 1 после удаления товара:")
store1.display_items()