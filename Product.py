class Product:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def pdisplay(self):
        print("Product Details:")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: {self.price}")

    def bdisplay(self):
        print("Bill:")
        # print(f"ID: {self.id}")
        # print(f"Name: {self.name}")
        # print(f"Quantity: {self.quantity}")
        # print(f"Price: {self.price}")
        # print(f"Total Bill: {self.quantity*self.price}")
        print(f"Total bill for {self.name} with quantity {self.quantity} is {self.quantity * self.price}")
        # return self.quantity*self.price
        print(f"ID      Name      Quantity      Price      Total Bill")
        print(
            f"{self.id}       {self.name}         {self.quantity}           {self.price}         {self.quantity * self.price}")


p1 = Product(1, "abc", 5, 60)
p1.pdisplay()
p2 = Product(2, "xyz", 8, 100)
p2.bdisplay()