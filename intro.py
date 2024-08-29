class Person:
  """Represents a person with name, age, and gender."""

  def __init__(self, name, age, gender):
    """Initializes a Person object.

    Args:
      name: The person's name.
      age: The person's age.
      gender: The person's gender.
    """
    self.name = name
    self.age = age
    self.gender = gender

  def introduce(self):
    """Prints an introductory message about the person."""
    print(f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.gender}.")

# Create an instance of the Person class
person1 = Person("Alice", 25, "female")

# Call the introduce method
person1.introduce()