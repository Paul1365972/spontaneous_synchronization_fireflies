from sim import Simulation
import numpy as np
import random
import time
import pandas as pd
import matplotlib.pyplot as plt


WIDTH, HEIGHT = 500, 500
FPS = 60

def run():
    simulation = Simulation(WIDTH, HEIGHT)
    for _ in range(100):
        rate = random.randint(FPS * 5, FPS * 5)
        simulation.add_firefly(rate, random.randint(0, rate), 100, 1, 0.08)
    data_points = []
    for _ in range(3_000):
        simulation.update()
        data_points.append(sum([1 for f in simulation.fireflies if f.blink_animation > 0]))

    fig, ax = plt.subplots()
    ax.plot(data_points, linestyle='-')
    ax.grid()
    ax.set_xlim((0, 3000))
    ax.set_xlabel('Simulationsschritt')
    ax.set_ylabel('# Blinkender Gühwürmchen')
    ax.set_title('Beispiel: Anzahl blinkender Gühwürmchen über den Verlauf der Simulation')
    plt.show()

run()
