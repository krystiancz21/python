from collections import namedtuple, defaultdict

Product = namedtuple('Product', ['name', 'price', 'weight'])

products = [
    Product(name="Banan", price="2.2", weight="110"),
    Product(name="Gruszka", price="3.2", weight="120"),
    Product(name="Kiwi", price="4.1", weight="80"),
    Product(name="Granat", price="6", weight="200"),
    Product(name="Jabłko", price="3.3", weight="190"),
    Product(name="Banan", price="2.5", weight="160"),
    Product(name="Gruszka", price="1.2", weight="90"),
    Product(name="Kiwi", price="4.8", weight="85"),
    Product(name="Granat", price="1", weight="180"),
    Product(name="Śliwka", price="7", weight="125"),
]

def sort_name(input):
    result_products = defaultdict(list)
    for item in input:
        result_products[item.name].append(item)
    return result_products


sorted_products = sort_name(products)

print("---- #3 ----")
for name, items in sorted_products.items():
    print(f"Nazwa: {name}:")
    for item in items:
        print(f" > {item.name} (Cena: {item.price}, Waga: {item.weight})")
