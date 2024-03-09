class Flowers:
    color = "цвет"
    freshness = "свежесть"
    height = "длинна стебля"
    price = "стоимость"
    name = "название цветка"

    def __init__(self, days_in_shop: int, height: int, long_live: int, color: str, price: int, name: str, val_fl: int):
        self.freshness = days_in_shop
        self.height = height
        self.long_live = long_live
        self.color = color
        self.price = price
        self.name = name
        self.val_fl = val_fl

    def freshness_level(self) -> str:
        if self.freshness <= 0:
            return "fresh"
        elif self.freshness <= 10:
            return "mid"
        elif self.freshness <= 20:
            return "mid_plus"
        else:
            return "old_free"

    def height_category(self) -> str:
        if self.height <= 10:
            return "low"
        elif self.height <= 30:
            return "mid"
        elif self.height <= 50:
            return "mid_plus"
        else:
            return "high"

    def longevity(self) -> str:
        if self.long_live <= 2:
            return "short_days_live"
        elif self.long_live <= 5:
            return "mid_days_live"
        elif self.long_live <= 10:
            return "long_days_live"
        else:
            return "long_plus_days_live"

    def color_uniqueness(self) -> str:
        if self.color == "purple":
            return "unusual"
        else:
            return "usual"


class HomeFlowers(Flowers):
    def __init__(self, str_days_in_shop_max_5, int_flowers_height, int_flowers_long_live, str_flowers_color,
                 int_flowers_price, str_flowers_name, needs_care, for_bouquets, val_fl):
        super().__init__(str_days_in_shop_max_5, int_flowers_height, int_flowers_long_live, str_flowers_color,
                         int_flowers_price, str_flowers_name, val_fl)
        self.needs_care = needs_care
        self.for_bouquets = for_bouquets


chinese_aster = HomeFlowers(5, 25, 7, "red",
                            10, "Chinese aster", True, True, 1)
cetunia = HomeFlowers(10, 25, 17, "white",
                      10, "Cetunia", True, True, 1)
clematis = HomeFlowers(1, 34, 27, "red",
                       10, "Clematis", True, True, 1)


class WildFlowers(Flowers):
    def __init__(self, str_days_in_shop_max_5, int_flowers_height, int_flowers_long_live, str_flowers_color,
                 int_flowers_price, str_flowers_name, medicinal_properties, toxicity, val_fl):
        super().__init__(str_days_in_shop_max_5, int_flowers_height, int_flowers_long_live, str_flowers_color,
                         int_flowers_price, str_flowers_name, val_fl)
        self.medicinal_properties = medicinal_properties
        self.toxicity = toxicity


goose_onion = WildFlowers(0, 25, 10, "purple",
                          13, "Goose onion", True, False, 1)
armeria = WildFlowers(2, 25, 20, "purple",
                      11, "Armeria", True, False, 1)
geranium = WildFlowers(6, 25, 5, "purple",
                       10, "Geranium", True, False, 1)


class Bouquet:
    def __init__(self):
        self.flowers = []  # Список цветов в букете

    def add_flower(self, flower, quantity):  # Добавляем цветок в список количество раз указанное quantity
        for _ in range(quantity):
            self.flowers.append(flower)

    def calculate_total_price(self):  # сумируем прайсы цветков добавленных выше в self.flowers = []
        return sum(flower.price for flower in self.flowers)

    def avg_time_bucket(self):  # считаем средню прод. жизни букета по flower.long_live / но кол-во видов в букете
        return sum(flower.long_live for flower in self.flowers) / len(self.flowers)

    def sort_bucket_color(self):  # сортировка букета по параметру Flovers.color = "цвет"
        # отбираем все цвета по каждой единице в букете
        color_list = sorted(flower.color for flower in self.flowers)
        unic_val = []
        # Добавляем уникальные значения из prise_list в список unic_val
        [unic_val.append(Flowers.color) for Flowers.color in color_list if Flowers.color
         not in unic_val]
        return unic_val

    def sort_bucket_freshness(self):  # сортировка букета по параметру Flovers.freshness = "свежесть"
        # отбираем все свежести по каждой единице в букете
        freshness_list = sorted(flower.freshness for flower in self.flowers)
        unic_val = []
        # Добавляем уникальные значения из prise_list в список unic_val
        [unic_val.append(Flowers.freshness) for Flowers.freshness in freshness_list if Flowers.freshness
         not in unic_val]
        return unic_val

    def sort_bucket_height(self):  # сортировка букета по параметру Flovers.height = "длинна стебля"
        # отбираем все длины по каждой единице в букете
        height_list = sorted(flower.height for flower in self.flowers)
        unic_val = []
        # Добавляем уникальные значения из height_list в список unic_val
        [unic_val.append(Flowers.height) for Flowers.height in height_list if Flowers.height not in unic_val]
        return unic_val  # возвращаем список уникальных значений

    def sort_bucket_price(self):  # сортировка букета по параметру Flovers.price = "цена"
        # отбираем все цены по каждой единице в букете
        prise_list = sorted(flower.price for flower in self.flowers)
        unic_val = []
        # Добавляем уникальные значения из prise_list в список unic_val
        [unic_val.append(Flowers.price) for Flowers.price in prise_list if Flowers.price not in unic_val]
        return unic_val  # возвращаем список уникальных значений

    # Поиск по параметрам
    def search_flower_by_param2(self, param):
        matching_flowers = []
        for flower in self.flowers:
            if param == flower.long_live:
                matching_flowers.append(flower.name)
            elif param == flower.height:
                matching_flowers.append(flower.name)
            elif param == flower.freshness:
                matching_flowers.append(flower.name)
            elif param == flower.color:
                matching_flowers.append(flower.name)
            else:
                return "Incorrect search params"
        return list(set(matching_flowers))


# Создаем объект класса Bouquet
my_bouquet = Bouquet()

# Добавляем цветы в букет вызывая вункцию Bucket add_flower, передаем цветы и их количество
my_bouquet.add_flower(chinese_aster, 5)
my_bouquet.add_flower(cetunia, 5)
my_bouquet.add_flower(goose_onion, 5)
my_bouquet.add_flower(armeria, 5)

# Вычисляем стоимость букета
total_price = my_bouquet.calculate_total_price()
print(f"Общая стоимость букета: {total_price}р.")

# Вычисляем среднее время жизни букета (по среднему времени жизни цветов букета)
avg_bucket_live = my_bouquet.avg_time_bucket()
print(f"Время увядания букета: {int(avg_bucket_live)}д.")

sort_bucket = my_bouquet.sort_bucket_color()  # вызов сортировки по цвету
print(f"Сортировка по параметру цвет - {sort_bucket}")

sort_bucket = my_bouquet.sort_bucket_freshness()  # вызов сортировки по свежести
print(f"Сортировка по параметру свежесть - {sort_bucket}")

sort_bucket = my_bouquet.sort_bucket_height()  # вызов сортировки по длинне стебля
print(f"Сортировка по параметру длинна стебля - {sort_bucket}")

sort_bucket = my_bouquet.sort_bucket_price()  # вызов сортировки по цене
print(f"Сортировка по параметру цена - {sort_bucket}")

search_flower = my_bouquet.search_flower_by_param2(25)  # поиск по параметру
print(f"Найден цветок - {search_flower}")
