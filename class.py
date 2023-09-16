class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed=None, color=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

    def description(self):
        details = f"{self.name} is {self.age} years old."
        if self.breed:
            details += f" They are a {self.breed}."
        if self.color:
            details += f" Their color is {self.color}."
        return details

    def speak(self, sound="Woof!"):
        return f"{self.name} says '{sound}'"

    def celebrate_birthday(self):
        self.age += 1
        return f"Today is {self.name}'s birthday! They are now {self.age} years old."

    def __str__(self):
        return f"{self.name} - {self.species}"

# Create instances of the Dog class with realistic information
dogs = [
    Dog("Buddy", 3, "Golden Retriever", "Golden"),
    Dog("Molly", 5, "Labrador", "Black"),
    Dog("Rex", 2, "Bulldog", "White"),
    Dog("Bella", 4, "Poodle", "Apricot"),
    Dog("Jack", 6, "Shih Tzu", "Brown")
]

# Display the list of dogs and their indices
print("Choose a dog by index:")
for i, dog in enumerate(dogs):
    print(f"{i}: {dog.name}")

# Prompt the user to select a dog by index
selected_index = int(input("Enter the dog's index: "))

# Check the selected index
if selected_index >= 0 and selected_index < len(dogs):
    selected_dog = dogs[selected_index]
    print("\nInformation about the selected dog:")
    print(selected_dog.description())
    print(selected_dog.speak())
    print(selected_dog.celebrate_birthday())
else:
    print("Invalid index. Please choose an existing dog.")
