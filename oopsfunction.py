class Items():
    

    def __init__(self,name,description,price):
        self.name = name
        self.description = description
        self.price = price
        
    def display(self):
        return f"product name:{self.name} description: {self.description} price: {self.price}"

product1 = Items("apple","royal",20)
print("Name:",product1.name)
print("description:",product1.description)
print("price:",product1.price)
print(product1.display())
product1.category = "it is not comman"



product2 = Items("orange","it is yellow color",70)
print("Name:",product2.name)
print("description:",product2.description)
print("price:",product2.price)
print(product2.display())
