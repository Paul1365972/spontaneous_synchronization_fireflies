import random

class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fireflies = []
        self.blinking_data = []

    def add_firefly(self, blink_rate, blink_timer, distance, speed):
        self.fireflies.append(Firefly(random.randint(0, self.width), random.randint(0, self.height), blink_rate, blink_timer, distance, speed))

    def update(self):
        self.update_move()
        self.update_blink()
        self.update_timer()

    def update_move(self):
        for firefly in self.fireflies:
            firefly.x += random.randint(-firefly.speed, firefly.speed)
            firefly.y += random.randint(-firefly.speed, firefly.speed)
            firefly.x = max(min(firefly.x, self.width), 0)
            firefly.y = max(min(firefly.y, self.height), 0)

    def update_blink(self):
        for firefly in self.fireflies:
            firefly.blinking = False
            firefly.blink_animation -= 1

            firefly.blink_timer -= 1
            if firefly.blink_timer <= 0:
                firefly.blinking = True
                firefly.blink_timer = firefly.blink_rate
                firefly.blink_animation = 20

    def update_timer(self):
        for firefly in self.fireflies:
            if firefly.blinking:
                for other in self.fireflies:
                    if firefly != other:
                        distance_sq = (firefly.x - other.x)**2 + (firefly.y - other.y)**2
                        other.blink_timer -= (distance_sq < other.distance ** 2) * (other.blink_rate - other.blink_timer) * 0.05

class Firefly:
    def __init__(self, x, y, blink_rate, blink_timer, distance, speed):
        self.x = x
        self.y = y
        self.blink_rate = blink_rate
        self.blink_timer = blink_timer
        self.distance = distance
        self.speed = speed
        self.blinking = False
        self.blink_animation = 0
