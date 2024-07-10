import pygame
import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
from sim import Simulation
import numpy as np


FPS = 60
WIDTH, HEIGHT = 500, 500

matplotlib.use("Agg")

pygame.init()
screen = pygame.display.set_mode((WIDTH * 2, HEIGHT))
pygame.display.set_caption("Firefly Simulation")
clock = pygame.time.Clock()


simulation = Simulation(WIDTH, HEIGHT)

for _ in range(100):
    simulation.add_firefly(FPS * random.randint(4, 6), random.randint(0, FPS * 5), 100, 1)

def update_graph_visuals():
    fig = plt.figure(figsize=(WIDTH/72, HEIGHT/72), dpi=72)
    ax = fig.add_subplot()
    ax.set_xlim((TICKS - FPS * 5, TICKS))
    ax.set_xlabel('Time (frames)')
    ax.set_ylabel('Blinking Fireflies')
    ax.grid()
    ax.plot(blinking_data)
    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()
    surface = pygame.image.fromstring(raw_data, size, "RGB")
    plt.close()
    return surface


running = True
fast_forward = False
plots_enabled = False
plot_surface = None
TICKS = 0
blinking_data = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fast_forward = not fast_forward
            elif event.key == pygame.K_p:
                plots_enabled = not plots_enabled

    # Step simulation
    simulation.update()

    # Render simulation
    screen.fill((48, 48, 64))
    dim_yellow, bright_yellow = np.array([50, 50, 0]), np.array([255, 255, 100])
    for firefly in simulation.fireflies:
        if firefly.blink_animation > 0:
            blink_strength = firefly.blink_animation / 20.0
            color = (dim_yellow * (1 - blink_strength) + bright_yellow * blink_strength).astype(int)
        else:
            color = np.array([0, 0, 0])
        pygame.draw.circle(screen, color.tolist(), (int(firefly.x), int(firefly.y)), 5)

    # Update logs
    blinking_count = sum([1 for f in simulation.fireflies if f.blink_animation > 0])
    blinking_data.append(blinking_count)

    # Render plots
    if plots_enabled:
        if plot_surface is None or TICKS % 10 == 0:
            plot_surface = update_graph_visuals()
        screen.blit(plot_surface, (WIDTH, 0))

    pygame.display.flip()
    clock.tick(FPS if not fast_forward else FPS * 10)
    TICKS += 1

pygame.quit()
