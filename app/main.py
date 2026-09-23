class Animal:
    alive = []
    def __init__(
            self,
            name_str,
            health_int=100,
            hidden_bool=False
    ):
        self.name = name_str
        self.health = health_int
        self.hidden = hidden_bool
        Animal.alive.append(self)
    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"
    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            Animal.alive.remove(self)

class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, prey: Animal):
        if isinstance(prey, Carnivore) or prey.hidden:
            return
        prey.take_damage(50)
