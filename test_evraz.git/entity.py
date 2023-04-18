class entity():
    def __init__(self, x_enemy, y_enemy, radius, shot, facing):
        self.x_enemy = x_enemy
        self.y_enemy = y_enemy
        self.shot = shot
        self.radius = radius
        self.facing = facing
        self.vel = 15 * facing