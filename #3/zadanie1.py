from collections import namedtuple

Product = namedtuple('Product', ['name', 'price', 'weight'])
# waga - gram

products = [
    Product(name="Banan", price="2.2", weight="110"),
    Product(name="Gruszka", price="3.2", weight="120"),
    Product(name="Kiwi", price="4.1", weight="80"),
    Product(name="Granat", price="6", weight="200"),
]

print("---- #1 ----")
print(f"Wszystkie produkty: {products}")

print("Nazwy produktów:")
for product in products:
    print(product.name)
