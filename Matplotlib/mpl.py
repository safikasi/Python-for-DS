import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create 3x3 grid of subplots
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(10, 8))
plt.tight_layout()

# Plot both sin(x) and cos(x) in every subplot
for current_ax in axes.flat:
    current_ax.plot(x, y_sin, color='orange', label='sin(x)')
    current_ax.plot(x, y_cos, color='magenta', label='cos(x)')  # different color and style
    current_ax.set_title('sin(x) & cos(x)')
    current_ax.legend(loc=10)  # show labels

plt.show()

# -------- Figure Size and DPI --------
fig = plt.figure(figsize=(5, 3))  # 5 inches wide, 3 inches tall
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x1, y1, 'b-')  # Plot using x1 and y1
ax.set_title('Figure with custom size')
plt.show()

# -------- One row, two columns of subplots --------
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 3))
axes[0].plot(x1, y1, 'g-')
axes[0].set_title('Left Plot')

axes[1].plot(x1, np.cos(x1), 'r--')
axes[1].set_title('Right Plot')

plt.tight_layout()
plt.show()
