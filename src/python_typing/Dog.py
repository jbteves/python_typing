"""This module implements a Dog."""

from beartype import beartype


class Dog:
    """A class that aids with woofing, petting, and more."""

    def __init__(self, name: str = "Fido") -> None:
        """Construct a dog with a given name."""
        self._name = name

    @property
    def name(self) -> str:
        """Get the dog's name."""
        return self._name

    def woof(self) -> None:
        """Has the dog woof."""
        print(f"{self.name} says \"Woof!\"")

    @beartype
    def pet(self, petter: str) -> None:
        """Pet the dog."""
        print(f"{petter} pets {self._name}")

    @beartype
    def play(self, player: str) -> None:
        """Play with the dog."""
        # First, we pet the dog to calm them down
        self.pet(player)
        print(f"{player} throws a frisbee and {self.name} catches it!")
