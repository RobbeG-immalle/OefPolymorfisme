import random

class Katachtige:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def GiveInfo(self):
        print(f"My name is {self.name}")

class Tijger(Katachtige):
    def __init__(self, name, age, sound = random.choice(["*RAAAAAAAWR*","*RAAAUCH*","*REEEEEEEE*"])):
        self.sound = sound
        super().__init__(name, age)
        # Katachtige.__init__(self, name, age)
        # super() Verwijst ook naar de parent class en doet eigelijk hetzelfde als de regel hierboven.

    def GiveInfo(self):
        Katachtige.GiveInfo(self)
        print(f"I'm a tiger and I'm {self.age} years old {self.sound}")
    
class Huiskat(Katachtige):
    def __init__(self, name, age, sound = random.choice(["*MIAUW*","*MEOOOOOOW*","*MEOWWWW*"])):
        self.sound = sound
        Katachtige.__init__(self, name, age)
        
    def GiveInfo(self):
        Katachtige.GiveInfo(self)
        print(f"I'm a Cat and I'm {self.age} years old {self.sound}")


class Shark:
    def __init__(self, age, color, food):
        self.age = age
        self.color = color
        self.food = food

class TigerShark(Shark):
    def __init__(self, age, color, food):
        super().__init__(age, color, food)
    
    def GiveInfo(self):
        print(f"I'm a Tiger shark I'm {self.age} years old, I'm {self.color} and I love eating {self.food}")

class Hammerhead(Shark):
    def __init__(self, age, color, food):
        super().__init__(age, color, food)

    def GiveInfo(self):
        print(f"I'm a Hammerhead shark I'm {self.age} years old, I'm {self.color} and I love eating {self.food}")


if __name__ == "__main__":
    k = Huiskat("Speedy", 10)
    t = Tijger("Tyler",17)
    k2 = Huiskat("Jeff", 1)

    ts = TigerShark(12,"Gray","Meat")
    hhs = Hammerhead(5, "Beige", "Humans")

    members = [k,t, k2,ts, hhs]
    for member in members:
        member.GiveInfo()
    


    