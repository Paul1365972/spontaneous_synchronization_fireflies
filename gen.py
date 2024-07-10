from sim import Simulation
import numpy as np
import random
import time


WIDTH, HEIGHT = 500, 500
FPS = 60

def run():
    simulation = Simulation(WIDTH, HEIGHT)
    for _ in range(100):
        simulation.add_firefly(FPS * 5, random.randint(0, FPS * 5), 100, 1)
    for i in range(60_000):
        simulation.update()
        if sum([1 for f in simulation.fireflies if f.blink_animation > 0]) > 90:
            return i
    return -1

start = time.time()

total_steps = 0
finish = 0
for _ in range(10):
    steps = run()
    if steps > 0:
        total_steps += steps
        finish += 1

print(f"Avg Steps: {total_steps / finish} ({finish} finished)")
print(f"Elapsed Time: {time.time() - start}")
