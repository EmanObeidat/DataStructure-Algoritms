class Animal: #represents an animal in the shelter.
    def __init__(self, species, name): #It has two properties: species (either "dog" or "cat") and name (string).
        self.species = species
        self.name = name

class AnimalShelter:
    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []

    def enqueue(self, animal): #It has two queues: dog_queue and cat_queue, which hold dogs and cats, respectively.
        '''
        If the species is "dog", the animal is appended to the dog_queue.
        If the species is "cat", the animal is appended to the cat_queue.

        '''
        if animal.species == "dog":
            self.dog_queue.append(animal)
        elif animal.species == "cat":
            self.cat_queue.append(animal)

    def dequeue(self, pref):
        if pref == "dog":
            if self.dog_queue:
                return self.dog_queue.pop(0)
        elif pref == "cat":
            if self.cat_queue:
                return self.cat_queue.pop(0)
        return None
# Create an instance of the AnimalShelter
shelter = AnimalShelter()

# Enqueue some animals
dog1 = Animal("dog", "Buddy")
shelter.enqueue(dog1)

cat1 = Animal("cat", "Whiskers")
shelter.enqueue(cat1)

dog2 = Animal("dog", "Max")
shelter.enqueue(dog2)

# Dequeue a dog
pref = "dog"
adopted_dog = shelter.dequeue(pref)
if adopted_dog:
    print(f"Adopted a {adopted_dog.species} named {adopted_dog.name}")
else:
    print("No dogs available for adoption.")

# Dequeue a cat
pref = "cat"
adopted_cat = shelter.dequeue(pref)
if adopted_cat:
    print(f"Adopted a {adopted_cat.species} named {adopted_cat.name}")
else:
    print("No cats available for adoption.")
