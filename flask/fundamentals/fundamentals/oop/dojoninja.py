class Ninja:
    def __init__ (self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print ('walking is great!')
        return self

    def feed(self):
        self.pet.eat()
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print ("Need More Food!")
        return self

    def bathe(self):
        self.pet.noise()
        print("oink")
        return self