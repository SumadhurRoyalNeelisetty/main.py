'''
class Client:
    name = "default"
    phone = "(123)456-7890"
    email = "abc@gmail.com"
    purchases = 0

def main():
    firstClient = Client()
    firstClient.name = "Sumadhur Royal"
    firstClient.email = "abc@gmail.com"
    print(firstClient.name)
    print(firstClient.phone)
    print(firstClient.email)
    print(firstClient.purchases)
main()
'''


'''
class Person:
    name="Sumadhur"
    def sayName(self):
        print("My name is ",self.name)

def main():
    x1 = Person()
    x1.sayName()
    x2 = Person()
    x2.sayName()
    x1.name="abc"
    x2.name="xyz"
    print(x1.name)
    print(x2.name)
main()
'''


'''
class Person:
	name="Nameless bird"
	def __init__(self, aName):
		self.name = aName
def main():
	aPerson = Person("Finder Wyvernspur")
	print(aPerson.name)
main()
'''