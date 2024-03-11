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
        self.freshness_level()
        self.height_category()
        self.longevity()
        self.color_uniqueness()

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


chinese_aster = HomeFlowers(4, 6, 7, "red",
                            1, "Chinese aster", True, True, 1)
cetunia = HomeFlowers(5, 5, 17, "white",
                      2, "Cetunia", True, True, 1)
clematis = HomeFlowers(6, 4, 27, "red",
                       3, "Clematis", True, True, 1)


class WildFlowers(Flowers):
    def __init__(self, str_days_in_shop_max_5, int_flowers_height, int_flowers_long_live, str_flowers_color,
                 int_flowers_price, str_flowers_name, medicinal_properties, toxicity, val_fl):
        super().__init__(str_days_in_shop_max_5, int_flowers_height, int_flowers_long_live, str_flowers_color,
                         int_flowers_price, str_flowers_name, val_fl)
        self.medicinal_properties = medicinal_properties
        self.toxicity = toxicity


goose_onion = WildFlowers(1, 3, 10, "purple",
                          4, "Goose onion", True, False, 1)
armeria = WildFlowers(2, 2, 20, "purple",
                      5, "Armeria", True, False, 1)
geranium = WildFlowers(3, 1, 5, "purple",
                       6, "Geranium", True, False, 1)


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

    """Синтаксис (общий для всех сортировок):
    sorted(iterable, key=None, reverse=False)
    iterable - последовательность, которую нужно отсортировать (например, список).
    key (необязательный) - функция, которая принимает элемент и возвращает значение, по которому будет производиться
    сортировка. По умолчанию сортировка происходит по самим элементам.
    reverse (необязательный) - если True, то сортировка будет в обратном порядке (по убыванию).
    """

    def sort_bucket_color(self):  # сортировка букета по параметру Flovers.color = "цвет"
        # отбираем все цвета по каждой единице в букете
        color_list = sorted(flower.color for flower in self.flowers)
        unic_val = []
        # Добавляем уникальные значения из prise_list в список unic_val
        [unic_val.append(Flowers.color) for Flowers.color in color_list if Flowers.color
         not in unic_val]
        return unic_val

    def sort_bucket_freshness(self):
        freshness_list = sorted(self.flowers, key=lambda flower: flower.freshness)  # т.е. для каждого flower
        # вернуть его flower.freshness
        flower_names = [flower.name for flower in freshness_list]
        names = []  # создаем пустой список и добавляем в него уникальные имена, по порядку из flower_names
        for name in flower_names:
            if name not in names:
                names.append(name)
        return names

    def sort_bucket_height(self):
        sorted_fl_by_height = sorted(self.flowers, key=lambda flower: flower.height)  # т.е. для каждого flower
        # вернуть его flower.height
        flower_names = [flower.name for flower in sorted_fl_by_height]
        names = []  # создаем пустой список и добавляем в него уникальные имена, по порядку из flower_names
        for name in flower_names:
            if name not in names:
                names.append(name)
        return names

    def sort_bucket_price(self):
        sorted_flowers = sorted(self.flowers, key=lambda flower: flower.price)  # т.е. для каждого flower
        # вернуть его flower.price
        flower_names = [flower.name for flower in sorted_flowers]  # вывести имена отсортированных flower
        # из sorted_flowers
        names = []  # создаем пустой список и добавляем в него уникальные имена, по порядку из flower_names
        for name in flower_names:
            if name not in names:
                names.append(name)
        return names

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
my_bouquet.add_flower(clematis, 5)
my_bouquet.add_flower(geranium, 5)

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
