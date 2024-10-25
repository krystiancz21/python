from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    weight: int # gram

products = [
    Product(name="Banan", price=2.2, weight=110),
    Product(name="Gruszka", price=3.2, weight=120),
    Product(name="Kiwi", price=4.1, weight=80),
    Product(name="Granat", price=6, weight=200),
]

print("---- #2 ----")
print(f"Wszystkie produkty: {products}")

print("Nazwy produktów:")
for product in products:
    print(product.name)

