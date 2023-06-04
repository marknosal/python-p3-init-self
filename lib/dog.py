class Dog:
    def __init__(self, name, breed='Mutt', favorite_toy='Anything'):
        self.name = name
        self.breed = breed
        self.favorite_toy = favorite_toy
        print(f'{name} has been born!')
    def bark(self):
        print("Woof!")
    def get_adopted(self, owner_name):
        self.owner = owner_name
        print(f'{self.name} has been adopted by {owner_name}!')


fido = Dog("Fido")
