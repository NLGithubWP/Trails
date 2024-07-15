import re
import json

# Load and parse the log file
with open("./internal/ml/model_slicing/exp_data/trails_log_folder/in_db_ms_1721048163.log", 'r') as file:
    log_contents = file.read()

# Find all occurrences of "final result" and extract the following dictionary
final_results = re.findall(r"final result = ({.*?})", log_contents)

# Parse each extracted dictionary and accumulate memory logs
all_memory_logs = []
cumulative_time = 0

for result in final_results:
    result_dict = json.loads(result.replace("'", '"'))  # Convert single quotes to double quotes for JSON parsing
    memory_log = json.loads(result_dict.get('memory_log', []))

    for entry in memory_log:
        cumulative_time += entry[0]
        all_memory_logs.append([cumulative_time, entry[1]])

# Prepare data for plotting
timestamps = [entry[0] for entry in all_memory_logs]
memory_usage = [entry[1] / 1024 for entry in all_memory_logs]  # Convert KB to MB

# Plotting the data
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


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

file_name = "micro_memory_sql_no_response"
print(f"saving to ./internal/ml/model_slicing/exp_imgs/{file_name}.pdf")
fig.savefig(f"./internal/ml/model_slicing/exp_imgs/{file_name}.pdf", bbox_inches='tight')
