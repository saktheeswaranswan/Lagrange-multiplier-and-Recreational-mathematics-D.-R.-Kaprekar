import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Step 1: Function to calculate sum of squares of digits
def sum_of_squares(n):
    return sum(int(digit) ** 2 for digit in str(n))

# Step 2: Function to find the Kaprekar cycle
def kaprekar_cycle(n):
    seen = []
    while n not in seen:
        seen.append(n)
        n = sum_of_squares(n)
    return seen

# Step 3: Input 11-digit multiplication
num1 = 12345678901  # Example input number 1
num2 = 10987654321  # Example input number 2
result = num1 * num2

# Calculate the Kaprekar cycle
cycle = kaprekar_cycle(result)

# Step 4: Visualization using Matplotlib
fig, ax = plt.subplots()
plt.title("Kaprekar Cycle Animation")
plt.xlabel("Step")
plt.ylabel("Sum of Squares")
line, = ax.plot([], [], 'ro-', markersize=8)
ax.grid(True)

def init():
    ax.set_xlim(0, len(cycle) + 1)
    ax.set_ylim(0, max(cycle) + 10)
    return line,

def update(frame):
    line.set_data(range(frame + 1), cycle[:frame + 1])
    return line,

ani = FuncAnimation(
    fig, update, frames=len(cycle), init_func=init, blit=True, interval=1000
)
