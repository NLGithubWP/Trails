import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Sample data, replace this with your actual data
memory_log = {
    "with all opt": [[0.011415665, 18640], [1.055175038, 181936], [2.880769471, 313752], [4.687268933, 314160],
                     [6.496921395, 315800], [8.323205138, 317624], [10.142881984, 321788], [11.949888364, 322908],
                     [13.763130105, 324920], [15.585750244, 327052], [17.395894147, 329612], [19.221604421, 331656],
                     [20.366825284, 332184]],
    "w/o state cache": [
        [0.0144259, 20804], [1.030951876, 184876], [2.909390436, 314468], [4.738563242, 315680],
        [6.553871011, 317364], [8.392857958, 319112], [9.408757094, 320844], [11.25468476, 323972],
        [13.08372853, 326176], [14.921665195, 327536], [16.741873756, 329992], [18.577636054, 331960],
        [20.396168183, 334424]
    ],
    # "w/o memory sharing": [
    #     [0.0144259, 20804], [1.030951876, 184876], [2.909390436, 314468], [4.738563242, 315680],
    #     [6.553871011, 317364], [8.392857958, 319112], [9.408757094, 320844], [11.25468476, 323972],
    #     [13.08372853, 326176], [14.921665195, 327536], [16.741873756, 329992], [18.577636054, 331960],
    #     [20.396168183, 334424]
    # ],
    # "w/o all opt": [
    #     [0.0144259, 20804], [1.030951876, 184876], [2.909390436, 314468], [4.738563242, 315680],
    #     [6.553871011, 317364], [8.392857958, 319112], [9.408757094, 320844], [11.25468476, 323972],
    #     [13.08372853, 326176], [14.921665195, 327536], [16.741873756, 329992], [18.577636054, 331960],
    #     [20.396168183, 334424]
    # ],
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
    timestamps = [x[0] for x in data]
    memory_usage = [x[1] / 1024 for x in data]  # Convert KB to MB

    ax.plot(timestamps, memory_usage, label=label, color=color, linestyle=line_style, marker='o', linewidth=2)

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
plt.show()
