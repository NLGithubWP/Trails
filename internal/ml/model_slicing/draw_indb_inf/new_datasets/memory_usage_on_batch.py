import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Sample data, replace this with your actual data

memory_log = {
    "with all opt": [["batch 1 done", 1.15592716, 172040], ["batch 2 done", 1.197314647, 172296],
                     ["batch 3 done", 1.248627524, 172296], ["batch 4 done", 1.295099816, 172296],
                     ["batch 5 done", 1.346204133, 172500], ["batch 6 done", 1.403212023, 172500],
                     ["batch 7 done", 1.458325593, 172512], ["batch 8 done", 1.509868854, 172644],
                     ["batch 9 done", 1.563654628, 172644], ["batch 10 done", 1.615676971, 172644],
                     ["batch 11 done", 1.665433105, 172820], ["batch 12 done", 1.71789154, 172820],
                     ["batch 13 done", 1.766701564, 172996], ["batch 14 done", 1.819430819, 172996],
                     ["batch 15 done", 1.868000141, 172996], ["batch 16 done", 1.919203618, 172996],
                     ["batch 17 done", 1.970338782, 172996], ["batch 18 done", 2.020942853, 173176],
                     ["batch 19 done", 2.067107044, 173176], ["batch 20 done", 2.114675102, 173176],
                     ["batch 21 done", 2.168729231, 173372], ["batch 22 done", 2.222064055, 173372],
                     ["batch 23 done", 2.269457767, 173552], ["batch 24 done", 2.320242421, 173724],
                     ["batch 25 done", 2.36439156, 173912], ["batch 26 done", 2.411534608, 174096],
                     ["batch 27 done", 2.461876813, 174096], ["batch 28 done", 2.511514371, 174284],
                     ["batch 29 done", 2.560947967, 174284], ["batch 30 done", 2.612354286, 174468],
                     ["batch 31 done", 2.665600317, 174468], ["batch 32 done", 2.715154777, 174468],
                     ["batch 33 done", 2.761803715, 174468], ["batch 34 done", 2.808533691, 174468],
                     ["batch 35 done", 2.854767841, 174656], ["batch 36 done", 2.906361462, 174656],
                     ["batch 37 done", 2.951844309, 174656], ["batch 38 done", 3.00418961, 174656],
                     ["batch 39 done", 3.054195679, 174656], ["batch 40 done", 3.103580043, 174656],
                     ["batch 41 done", 3.155066616, 174656], ["batch 42 done", 3.207934763, 174828],
                     ["batch 43 done", 3.263164826, 174828], ["batch 44 done", 3.313752329, 175200],
                     ["batch 45 done", 3.363566957, 175200], ["batch 46 done", 3.413180567, 175200],
                     ["batch 47 done", 3.46364488, 175200], ["batch 48 done", 3.517716513, 175200],
                     ["batch 49 done", 3.5607830099999997, 175200], ["batch 50 done", 3.612313749, 175200],
                     ["batch 51 done", 3.662209437, 175200], ["batch 52 done", 3.709823296, 175376],
                     ["batch 53 done", 3.76163774, 175376], ["batch 54 done", 3.813391232, 175376],
                     ["batch 55 done", 3.864696331, 175484], ["batch 56 done", 3.914357926, 175484],
                     ["batch 57 done", 3.9617895279999997, 175484], ["batch 58 done", 4.013999969, 175484],
                     ["batch 59 done", 4.064732863, 175484], ["batch 60 done", 4.1176521170000004, 175484],
                     ["batch 61 done", 4.169715847, 175484], ["batch 62 done", 4.216280933, 175484],
                     ["batch 63 done", 4.2682276869999995, 175660], ["batch 64 done", 4.31963685, 175660],
                     ["batch 65 done", 4.368786991, 175660], ["batch 66 done", 4.420940952, 175660],
                     ["batch 67 done", 4.480295498, 175860], ["batch 68 done", 4.530193065, 175860],
                     ["batch 69 done", 4.58357945, 175860], ["batch 70 done", 4.636534113, 175860],
                     ["batch 71 done", 4.688402106, 175860], ["batch 72 done", 4.734265209, 175860],
                     ["batch 73 done", 4.786384857, 176056], ["batch 74 done", 4.8365828109999995, 176252],
                     ["batch 75 done", 4.893810123, 176252], ["batch 76 done", 4.939277636, 176252],
                     ["batch 77 done", 4.990833261, 176252], ["batch 78 done", 5.05056933, 176252],
                     ["batch 79 done", 5.096791671, 176252], ["batch 80 done", 5.139055328, 176252],
                     ["batch 81 done", 5.187139209, 176252], ["batch 82 done", 5.237290151, 176452],
                     ["batch 83 done", 5.290466887, 176452], ["batch 84 done", 5.341940428, 176452],
                     ["batch 85 done", 5.399539403, 176452], ["batch 86 done", 5.449329831, 176452],
                     ["batch 87 done", 5.5022920079999995, 176452], ["batch 88 done", 5.551156612, 176652],
                     ["batch 89 done", 5.60088477, 176652], ["batch 90 done", 5.650745579, 176652],
                     ["batch 91 done", 5.698332475, 176652], ["batch 92 done", 5.751479464, 176652],
                     ["batch 93 done", 5.798375089, 176652], ["batch 94 done", 5.8454405210000004, 176652],
                     ["batch 95 done", 5.894519659, 176848], ["batch 96 done", 5.9495856190000005, 176848],
                     ["batch 97 done", 5.997794264, 177044], ["batch 98 done", 6.04893706, 177220],
                     ["batch 99 done", 6.098659583, 177220], ["batch 100 done", 6.150192476, 177420]],
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
