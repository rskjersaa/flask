import dojoninja
# class Ninja:
#     def __init__ (self, first_name, last_name, treats, pet_food, pet):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.treats = treats
#         self.pet_food = pet_food
#         self.pet = pet

#     def walk(self):
#         self.pet.play()
#         print ('walking is great!')
#         return self

#     def feed(self):
#         self.pet.eat()
#         if len(self.pet_food) > 0:
#             food = self.pet_food.pop()
#             print(f"Feeding {self.pet.name} {food}!")
#             self.pet.eat()
#         else:
#             print ("Need More Food!")
#         return self

#     def bathe(self):
#         self.pet.noise()
#         print("oink")
#         return self

class Pet:
    def __init__ (self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 50
        self.energy = 100
        

    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 10
        return self

    def noise(self):
        print("oink")
        return self

my_treats=['pickles, bacon, huckleberries']
my_pet_food = ['kibble, chicken, rice']

fido = Pet("Mr. Fido", "dog", ['fetch', 'hunt'])

phil = dojoninja.Ninja("mojo","skjersaa", my_treats, my_pet_food, fido)


phil.feed().walk().bathe()

# print(fido.noise())
# phil.bathe()
# print(phil.feed())