from csv import DictReader, writer
from os import system


class Product:
    def __init__(self, id: str, name: str, desc: str, price: str, quantity: str) -> None:
        self.id = id
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity


    def __str__(self) -> str:           
        return f"{self.id} | {self.name} | {self.desc} | {self.price} | {self.quantity}"


class Inventory: 
    def __init__(self, products=None) -> None:
        if products is None:
            products = []
        self.products = products


    def check_inventory(self):
        system("cls")
        for product in self.products: 
            print(product)


    def add_item(self, id: str, name: str, desc: str, price: int, quantity: str):
        product = Product(id, name, desc, price, quantity)
        self.products.append(product)
        self.save_item("products.csv", id, name, desc, price, quantity)

    
    @staticmethod
    def load_inventory(filename): 
        products = []
    
        with open(filename, 'r') as file:
            reader = DictReader(file)

            for row in reader:
                id = int(row['id'])
                name = row['name']
                desc = row['desc']
                price = float(row['price'])
                quantity = int(row['quantity'])
                
                products.append(Product(id, name, desc, price, quantity))

        return products


def main(): 
    loaded_products = Inventory.load_inventory("products.csv")

    inventory = Inventory(loaded_products)
    inventory.check_inventory()
    inventory.add_item(len(loaded_products), "Mouse PRO click", "A cool mouse", 598, 10)
    inventory.check_inventory()


if __name__ == "__main__": 
     main()

