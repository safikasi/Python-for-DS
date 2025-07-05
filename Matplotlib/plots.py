import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# -------- 3x3 Grid of Line Plots --------
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(10, 8))

for current_ax in axes.flat:
    current_ax.plot(
        x, y_sin,
        color='orange',
        linewidth=2,
        alpha=1,
        linestyle='--',
        marker='o',
        label='sin(x)'
    )
    current_ax.plot(
        x, y_cos,
        color='magenta',
        linewidth=2,
        alpha=1,
        linestyle='--',
        label='cos(x)'
    )
    current_ax.set_title('sin(x) & cos(x)')
    current_ax.legend(loc='upper right')

plt.tight_layout()
plt.show()

# -------- Scatter Plot Example --------
x_vals = np.random.rand(100)
y_vals = np.random.rand(100)

plt.figure(figsize=(6, 4))
plt.scatter(x_vals, y_vals, color='teal', marker='x', alpha=0.7)
plt.title('Scatter Plot')
plt.xlabel('Random X')
plt.ylabel('Random Y')
plt.grid(True)
plt.show()

# -------- Box Plot Example --------
data1 = np.random.normal(loc=0, scale=1, size=100)
data2 = np.random.normal(loc=2, scale=1.5, size=100)
data3 = np.random.normal(loc=-1, scale=0.5, size=100)

plt.figure(figsize=(6, 4))
plt.boxplot([data1, data2, data3], labels=['Group 1', 'Group 2', 'Group 3'])
plt.title('Box Plot')
plt.ylabel('Values')
plt.grid(True)
plt.show()
