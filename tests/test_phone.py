from src.item import Item
from src.phone import Phone

phone_1 = Phone('test_phone', 20000, 20, 2)
item_1 = Item('test_item', 10000, 7)


def test_phone_init():
    assert phone_1.name == 'test_phone'
    assert phone_1.price == 20000
    assert phone_1.quantity == 20
    assert phone_1.number_of_sim == 2


def test_phone_add():
    assert item_1 + phone_1 == 27
    assert phone_1 + phone_1 == 40
    assert phone_1 + 6 is None