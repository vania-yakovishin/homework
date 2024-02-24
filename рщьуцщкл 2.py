class Cat:
    def init(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.energy = 50
    def meow(self):
        return "Meow!"
    def sleep(self):
        self.energy += 10
        return f"{self.name} is sleeping. Energy level: {self.energy}"
    def play(self):
        if self.energy >= 20:
            self.energy -= 20
            return f"{self.name} is playing and having fun!"
        else:
            return f"{self.name} is too tired to play."