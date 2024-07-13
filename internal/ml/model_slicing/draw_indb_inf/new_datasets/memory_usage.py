import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Sample data, replace this with your actual data
memory_log = [[1.16e-7, 19448], [1.7e-7, 192612], [1.85e-7, 313924], [8.3e-8, 315308], [8.5e-8, 318824],
              [1.86e-7, 320112],
              [1.16e-7, 322260], [1.03e-7, 324720], [2.5e-7, 327232], [9e-8, 327368], [9.1e-8, 329344],
              [9.1e-8, 332600],
              [1.98e-7, 335080]]

# Convert timestamps to seconds and memory usage to MB
timestamps = [x[0] * 1e7 for x in memory_log]  # Convert to seconds (assumption based on original data)
memory_usage = [x[1] / 1024 for x in memory_log]  # Convert KB to MB


# Helper function for formatting the y-axis
def thousands_formatter(x, pos):
    return '{:.1f} MB'.format(x)


# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(timestamps, memory_usage, label='Memory Usage', color='blue', marker='o', linestyle='-', linewidth=2)

# Formatting the y-axis
ax.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

# Adding labels and title
ax.set_xlabel('Time (s)', fontsize=14)
ax.set_ylabel('Memory Usage (MB)', fontsize=14)
ax.set_title('Memory Usage Over Time', fontsize=16)
ax.grid(True, linestyle='--', linewidth=0.5)

# Show legend
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()
