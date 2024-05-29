#INHERITENCE IN PYTHON!!!!
class Animal:
    alive = True
    
    def eat(self):
        print("this animal is eating")
    def sleep(self):
        print("this animal is sleeping")
    def hunt(self):
        print("this animal is going for hunt!!!")

class Lion(Animal):
    def hunting(self):
        print("lion is hunting!")
class Seal(Animal):
    def swim(self):
        print("seal is swiming!")
class Eagle(Animal):
    def fly(self):
        print("eagle is flying!")
#let's create some objects!
lion = Lion()
seal = Seal()
eagle = Eagle()
print(Lion.alive)
print(Seal.alive)
lion.eat()
lion.hunt()
seal.sleep()
eagle.eat()
lion.hunting()
seal.swim()
eagle.fly()
