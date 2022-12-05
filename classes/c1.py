class Cat:
    name = ""
    age = 0
    furcolor = ""
    breed = ""

    def eat(self):
        print("Cat is eating!")

    def sleep(self):
        print("Cat is sleeping!")

# creating objects
tom = Cat()
snow = Cat()
tom.name = "Tom"
tom.age = 3
tom.furcolor = 'gray'
tom.breed = "City Cat"
snow.name = "Snowbell"
snow.age = 5
snow.furcolor = "white"
snow.breed = "Persian"

#calling methods
tom.eat()
snow.sleep()
tom.sleep()

#displaying attributes
print(tom.name,tom.age,tom.furcolor,tom.breed)
print(snow.name,snow.age,snow.furcolor,snow.breed)

