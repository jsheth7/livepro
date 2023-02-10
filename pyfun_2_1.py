def __init__(self, part_number, price):
    self.price = price
    self.part_number = part_number

def get_price(self):
    return  self.price

namespace = {'__init__': __init__, 'get_price': get_price}

Price2 = type('Price2', (), namespace)

"""Try this out"""
# >>> import pyfun_2_1 as price_flat
# >>> p2 = price_flat.Price2(5, 10)
# >>> p2.get_price()
# 10
# >>> p2.part_number
# 5
