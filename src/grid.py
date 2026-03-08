import random

from src.pickups import Item


class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36
    height = 12
    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig vägg
    chest = "O"  # Tecken för en kista

    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]


    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs


    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

    def add_interior_walls(self):
        """Skapa några väggar inne i spelplanen"""
        for i in range(self.height):
            random_empty_x= self.get_random_corridor_x()
            random_empty_y= self.get_random_empty_y()

            self.set(random_empty_x, random_empty_y, self.wall)

    def if_next_to_wall(self, x, y):
        """Returnerar True om det finns en vägg i närheten av positionen (x, y) horisontellt"""
        return self.is_wall(x-1, y) or self.is_wall(x+1, y)


    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_corridor_x(self):
        """Slumpa en x-position på spelplanen som inte är intill en vägg och har en vägg två rutor bort horisontellt"""
        while True:
            x = random.randint(0, self.width-1)
            y = self.get_random_y()
            if self.is_empty(x, y) and not self.if_next_to_wall(x, y) and self.has_nearby_wall_with_vertical_clearance(x, y):
                return x

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)

    def get_random_empty_y(self):
        """Slumpa en y-position på spelplanen"""
        while True:
            x = self.get_random_x()
            y = random.randint(0, self.height-1)
            if self.is_empty(x, y):
                return y

    def has_nearby_wall_with_vertical_clearance(self, x, y):
        """Returnerar True om det finns en vägg två rutor bort horisontellt
        och inga väggar vertikalt intill mellanpositionen"""

        # Kontrollera vägg två steg till vänster
        if self.is_wall(x - 2, y):
            # Kontrollera att det inte finns väggar vertikalt vid x-1
            if not self.is_wall(x - 1, y - 1) and not self.is_wall(x - 1, y + 1):
                return True

        # Kontrollera vägg två steg till höger
        if self.is_wall(x + 2, y):
            # Kontrollera att det inte finns väggar vertikalt vid x+1
            if not self.is_wall(x + 1, y - 1) and not self.is_wall(x + 1, y + 1):
                return True

        return False

    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty

    def is_wall(self, x, y):
        """Returnerar True om det finns en vägg på aktuell ruta"""
        return self.get(x, y) == self.wall

    def is_chest(self, x, y):
        """Returnerar True om det finns en kista på aktuell ruta"""
        return self.get_symbol(self.get(x, y)) == self.chest

    def is_surrounding_wall(self, x, y):
        """Returnerar True om det finns en vägg i närheten av positionen (x, y) vertikalt eller horisontellt"""
        if x==0 or y==0 or x==self.width-1 or y==self.height-1:
            return True

        return False

    def get_symbol(self, param: Item):
        if isinstance(param, Item):
            return param.symbol
        return None
