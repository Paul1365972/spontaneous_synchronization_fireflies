from sim import Simulation
import numpy as np
import random
import time
import pandas as pd


WIDTH, HEIGHT = 500, 500
FPS = 60

def run(timer_offset, coupling):
    simulation = Simulation(WIDTH, HEIGHT)
    for _ in range(100):
        rate = random.randint(FPS * 5, int(FPS * (5 + timer_offset)))
        simulation.add_firefly(rate, random.randint(0, rate), 100, 1, coupling)
    for i in range(6_000):
        simulation.update()
        if sum([1 for f in simulation.fireflies if f.blink_animation > 0]) > 90:
            return i
    return -1

start = time.time()

data_points = []
for timer_offset in np.linspace(0, 5, 11):
    for coupling in np.linspace(0, 0.5, 11):
        total_steps = 0
        finish = 0
        for _ in range(10):
            steps = run(timer_offset, coupling)
            if steps >= 0:
                total_steps += steps
                finish += 1
        print(f"[{coupling}, {timer_offset}] Steps: {total_steps} ({finish} finished)")
        data_points.append({'coupling': coupling, 'timer_offset': timer_offset, 'steps': total_steps, 'finished': finish})

df = pd.DataFrame(data_points).round(10)
df.to_csv('data_points.csv')

print(f"Elapsed Time: {time.time() - start}")
