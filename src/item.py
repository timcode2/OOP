import csv
import os


class InstantiateCSVError(Exception):
    """Класс ошибки при открытии файла CSV"""

    def __init__(self, massage) -> None:
        self.massage = massage
        self.massage = 'Файл item.csv поврежден'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    file_name = 'items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        # Добавляем созданный экземпляр класса в список instances
        self.all.append(self)
        super().__init__()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            return "Длина наименования товара превышает 10 символов."

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        way_csv = os.path.join(os.path.dirname(__file__), cls.file_name)
        if not os.path.exists(way_csv):
            raise FileNotFoundError('Отсутствует файл item.csv')
        with open(way_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if 'name' not in reader.fieldnames or 'price' not in reader.fieldnames or 'quantity' not in reader.fieldnames:
                raise InstantiateCSVError('Файл item.csv поврежден')
            for row in reader:
                name, price, quantity = row['name'], row['price'], row['quantity']
                cls(name, float(price), int(quantity))

    @staticmethod
    def string_to_number(string):
        if '.' in string:
            return int(float(string))
        else:
            return int(string)
