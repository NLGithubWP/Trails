import re
import json
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Load and parse the log file
file_path = "./internal/ml/model_slicing/exp_data/trails_log_folder/rust_res.json"
with open(file_path, 'r') as file:
    log_contents = file.readlines()

# Parse each JSON line and accumulate memory logs
all_memory_logs = []
cumulative_time = 0

for line in log_contents:
    result_dict = json.loads(line)
    memory_log = json.loads(result_dict.get('memory_log', '[]'))

    for entry in memory_log:
        cumulative_time += entry[1]
        all_memory_logs.append([cumulative_time, entry[2]])

# Prepare data for plotting
timestamps = [entry[0] for entry in all_memory_logs]
memory_usage = [entry[1] / 1024 for entry in all_memory_logs]  # Convert KB to MB

# Helper function for formatting the y-axis
def mb_formatter(x, pos):
    return '{:.1f}'.format(x)

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 3))

# Plot the memory usage over time
ax.plot(timestamps, memory_usage, label='Memory Usage', color='blue', linestyle='-')

# Adding labels and title
ax.set_xlabel('Time (s)', fontsize=14)
ax.set_ylabel('Memory Usage (MB)', fontsize=14)
ax.grid(True, linestyle='--', linewidth=0.5)

# Formatting the y-axis
ax.yaxis.set_major_formatter(FuncFormatter(mb_formatter))

# Show legend
ax.legend()

# Display the plot
plt.tight_layout()

# Save the plot
file_name = "micro_memory_sql_nothing_record_only"
output_path = f"./internal/ml/model_slicing/exp_imgs/{file_name}.pdf"
print(f"saving to {output_path}")
fig.savefig(output_path, bbox_inches='tight')

