import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Constants
G = 6.67430e-11
M = 5.972e24
R = 6371000

# Initial position (400 km above Earth)
altitude = 400000
x = R + altitude
y = 0

# Initial velocity
vx = 0
vy = 7670

dt = 1
steps = 8000

positions_x = []
positions_y = []
distance = []

for i in range(steps):

    r = np.sqrt(x**2 + y**2)

    ax = -G * M * x / r**3
    ay = -G * M * y / r**3

    vx += ax * dt
    vy += ay * dt

    x += vx * dt
    y += vy * dt

    positions_x.append(x)
    positions_y.append(y)
    distance.append(r)

# Orbit Plot
fig, ax = plt.subplots()

earth = Circle((0,0), R, color='Green')
ax.add_patch(earth)

ax.plot(positions_x, positions_y, color='red')

ax.set_aspect('equal')
ax.set_title("Satellite Orbit Simulation")
ax.set_xlabel("X Position (m)")
ax.set_ylabel("Y Position (m)")

plt.show()

# Distance Graph
plt.figure()
plt.plot(distance)
plt.title("Satellite Distance from Earth")
plt.xlabel("Time Step")
plt.ylabel("Distance (m)")
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
G = 6.67430e-11
M = 5.972e24
R = 6371000

# Initial satellite conditions
altitude = 400000
x = R + altitude
y = 0

vx = 0
vy = 7670

dt = 1
steps = 5000

positions_x = []
positions_y = []

# Simulation
for i in range(steps):

    r = np.sqrt(x**2 + y**2)

    ax = -G * M * x / r**3
    ay = -G * M * y / r**3

    vx += ax * dt
    vy += ay * dt

    x += vx * dt
    y += vy * dt

    positions_x.append(x)
    positions_y.append(y)

# Plot setup
fig, ax = plt.subplots()

earth = plt.Circle((0,0), R, color='blue')
ax.add_patch(earth)

line, = ax.plot([], [], 'r-', lw=2)
satellite, = ax.plot([], [], 'ro')

ax.set_aspect('equal')
ax.set_xlim(-1.2*(R+altitude), 1.2*(R+altitude))
ax.set_ylim(-1.2*(R+altitude), 1.2*(R+altitude))

ax.set_title("Animated Satellite Orbit")
ax.set_xlabel("X Position (m)")
ax.set_ylabel("Y Position (m)")

# Animation function
def update(frame):
    line.set_data(positions_x[:frame], positions_y[:frame])
    satellite.set_data(positions_x[frame], positions_y[frame])
    return line, satellite

ani = FuncAnimation(fig, update, frames=len(positions_x), interval=10)

plt.show()