import string


def format_price(price):
    int_price = int(price)
    price_str = f'"Цена: {int_price} руб."'
    return price_str

res = format_price(56.24)
print(res)
    