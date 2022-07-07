from python_typing import Dog, mathemagic

# Store a Dog in a variable expecting an int
x: int = Dog()
# No error! No actual protection.

# Let's use something more sensible as a variable name
fido: Dog = Dog()
# the pet() method expects a name, but let's give it a number since we can
# do what we want!
#fido.pet(5)
# beartype roar! This method is runtime type-protected by beartype.

thing: dict[str, str] = {"dog": fido.name}
