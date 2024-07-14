import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Sample data, replace this with your actual data

memory_log = {
    "with all opt": 
}


# Helper function for formatting the y-axis
def mb_formatter(x, pos):
    return '{:.1f} MB'.format(x)


# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Define colors for different lines
colors = ['blue', 'green', 'red', 'purple']
# Define line styles for different lines
line_styles = ['-', '--', '-.', ':']

# Plot each configuration
for (label, data), color, line_style in zip(memory_log.items(), colors, line_styles):
    # Convert memory usage to MB
    timestamps = [int(x[0].split(" ")[1]) for x in data]
    memory_usage = [x[2] / 1024 for x in data]  # Convert KB to MB

    # Plot monitoring points
    monitoring_timestamps = [x[1] for x in data]
    monitoring_memory_usage = [x[2] / 1024 for x in data]
    ax.plot(monitoring_timestamps, monitoring_memory_usage, label=label, color=color, linestyle=line_style, marker='o')

    # # Plot "After batch" points
    # batch_timestamps = [x[1] for x in data if x[0].startswith("After batch")]
    # batch_memory_usage = [x[2] / 1024 for x in data if x[0].startswith("After batch")]
    # ax.scatter(batch_timestamps, batch_memory_usage, color=color, s=100, edgecolors='black', zorder=5)

# Formatting the y-axis
ax.yaxis.set_major_formatter(FuncFormatter(mb_formatter))

# Adding labels and title
ax.set_xlabel('Time (s)', fontsize=14)
ax.set_ylabel('Memory Usage (MB)', fontsize=14)
ax.set_title('Memory Usage Over Time', fontsize=16)
ax.grid(True, linestyle='--', linewidth=0.5)

# Show legend
ax.legend()

# Display the plot
plt.tight_layout()
# plt.show()

# Save the plot
print(f"saving to ./internal/ml/model_slicing/exp_imgs/micro_memory_batch.pdf")
fig.savefig(f"./internal/ml/model_slicing/exp_imgs/micro_memory_batch.pdf", bbox_inches='tight')
