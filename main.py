import pygame
import random
import math


pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Firefly Simulation")

FPS = 60

class Firefly:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 5
        self.blink_rate = FPS * 5
        self.blink_timer = random.randint(0, self.blink_rate)
        self.blink_animation = 0

    # Move brownian motion and keep inside bounds
    def update_move(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

        self.x = max(min(self.x, WIDTH - self.size), self.size)
        self.y = max(min(self.y, HEIGHT - self.size), self.size)

    # Update own blinking state
    def update_blink(self):
        self.blinking = False
        self.blink_animation -= 1

        if self.blink_timer <= 0:
            self.blinking = True
            self.blink_timer = self.blink_rate
            self.blink_animation = 10

    # Update iteractions with each other
    def update_timer(self, fireflies):
        self.blink_timer -= 1
        for other in fireflies:
            if self != other:
                distance = self.distance_to(other)
                self.blink_timer -= distance < 100 * other.blinking * (self.blink_rate - self.blink_timer) * 0.05

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def draw(self):
        color = (255, 255, 100) if self.blink_animation > 0 else (0, 0, 0)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.size)


# Create fireflies
fireflies = [Firefly(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(100)]


# Main loop
running = True
fast_forward = False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fast_forward = not fast_forward

    screen.fill((48, 48, 64))

    # Update and draw fireflies
    for firefly in fireflies:
        firefly.update_move()

    for firefly in fireflies:
        firefly.update_blink()

    for firefly in fireflies:
        firefly.update_timer(fireflies)

    for firefly in fireflies:
        firefly.draw()

    pygame.display.flip()
    clock.tick(FPS if not fast_forward else FPS * 10)

pygame.quit()
