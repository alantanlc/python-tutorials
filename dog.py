class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return f'{self.name} is {self.age} years old.'

    # instance method
    def speak(self, sound):
        return f'{self.name} says {sound}'

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'

class Snake(Dog):
    species = 'reptile'

def get_biggest_number(*args):
    return max(args)

if __name__ == '__main__':
    scooby = Dog('scooby', 99)
    bolt = Dog('bolt', 10)
    
    print(scooby == bolt)

    # Access the instance attributes
    print(f'{scooby.name} is {scooby.age} and {bolt.name} is {bolt.age}.')

    # Is Scooby a mammal?
    if scooby.species == 'mammal':
        print(f'{scooby.name} is a {scooby.species}!')

    print(get_biggest_number(scooby.age, bolt.age))

    # call our instance methods
    print(scooby.description())
    print(scooby.speak('Scooby dooby doo'))

    russell = RussellTerrier('Russell', 25)

    print(russell.run('slowly'))

    # Is Russell an instance of Dog()?
    print(isinstance(russell, Dog))

    # Is Russell an instance of Bulldog()?
    print(isinstance(russell, Bulldog))

    snake = Snake('sliss', 1)
    print(russell.species)
    print(snake.species)