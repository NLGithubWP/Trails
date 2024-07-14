import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Sample data, replace this with your actual data

memory_log = {
    "with all opt": [["batch 1 done", 1.106437471, 172284], ["batch 2 done", 1.160538345, 172540],
                     ["batch 3 done", 1.213388069, 172648], ["batch 4 done", 1.267707101, 172648],
                     ["batch 5 done", 1.308330316, 172700], ["batch 6 done", 1.356804749, 172700],
                     ["batch 7 done", 1.412697311, 172896], ["batch 8 done", 1.459772597, 173064],
                     ["batch 9 done", 1.51496584, 173064], ["batch 10 done", 1.5633032199999999, 173128],
                     ["batch 11 done", 1.613511503, 173128], ["batch 12 done", 1.6639961410000002, 173128],
                     ["batch 13 done", 1.711865889, 173128], ["batch 14 done", 1.763159633, 173408],
                     ["batch 15 done", 1.81122306, 173600], ["batch 16 done", 1.856801194, 173776],
                     ["batch 17 done", 1.907334294, 173776], ["batch 18 done", 1.9598129690000001, 173776],
                     ["batch 19 done", 2.012045841, 173776], ["batch 20 done", 2.063236799, 173776],
                     ["batch 21 done", 2.113849681, 173776], ["batch 22 done", 2.161968618, 173776],
                     ["batch 23 done", 2.209814032, 173776], ["batch 24 done", 2.264275623, 173776],
                     ["batch 25 done", 2.312939765, 173968], ["batch 26 done", 2.366797728, 173968],
                     ["batch 27 done", 2.416378899, 173968], ["batch 28 done", 2.467078549, 173968],
                     ["batch 29 done", 2.519154621, 173968], ["batch 30 done", 2.5682384369999998, 173968],
                     ["batch 31 done", 2.615679918, 174144], ["batch 32 done", 2.665978499, 174144],
                     ["batch 33 done", 2.7121906510000002, 174144], ["batch 34 done", 2.761030271, 174144],
                     ["batch 35 done", 2.816963052, 174144], ["batch 36 done", 2.868708989, 174144],
                     ["batch 37 done", 2.920415592, 174144], ["batch 38 done", 2.972417589, 174144],
                     ["batch 39 done", 3.017679158, 174336], ["batch 40 done", 3.066486853, 174336],
                     ["batch 41 done", 3.119066892, 174336], ["batch 42 done", 3.168054219, 174336],
                     ["batch 43 done", 3.2203918910000002, 174336], ["batch 44 done", 3.267084843, 174336],
                     ["batch 45 done", 3.317868591, 174336], ["batch 46 done", 3.368691125, 174524],
                     ["batch 47 done", 3.414127294, 174524], ["batch 48 done", 3.466874726, 174724],
                     ["batch 49 done", 3.52002869, 174908], ["batch 50 done", 3.5749393339999997, 174908],
                     ["batch 51 done", 3.626958042, 175104], ["batch 52 done", 3.677978963, 175104],
                     ["batch 53 done", 3.72606571, 175104], ["batch 54 done", 3.774821888, 175104],
                     ["batch 55 done", 3.823659916, 175104], ["batch 56 done", 3.86988909, 175104],
                     ["batch 57 done", 3.918222888, 175104], ["batch 58 done", 3.970132658, 175104],
                     ["batch 59 done", 4.023405997, 175296], ["batch 60 done", 4.074176408, 175488],
                     ["batch 61 done", 4.129259134, 175488], ["batch 62 done", 4.1833333, 175680],
                     ["batch 63 done", 4.231607635, 175680], ["batch 64 done", 4.279548902, 175680],
                     ["batch 65 done", 4.327266264, 175680], ["batch 66 done", 4.378319009, 175680],
                     ["batch 67 done", 4.428967634, 175880], ["batch 68 done", 4.48188607, 175880],
                     ["batch 69 done", 4.5356363, 175880], ["batch 70 done", 4.5837552089999996, 175880],
                     ["batch 71 done", 4.629386068, 176068], ["batch 72 done", 4.680557466, 176068],
                     ["batch 73 done", 4.732454258, 176068], ["batch 74 done", 4.783840361, 176264],
                     ["batch 75 done", 4.838606675, 176444], ["batch 76 done", 4.888334136, 176444],
                     ["batch 77 done", 4.937376116, 176444], ["batch 78 done", 4.982507941, 176444],
                     ["batch 79 done", 5.036313705, 176444], ["batch 80 done", 5.08796648, 176444],
                     ["batch 81 done", 5.132357849, 176444], ["batch 82 done", 5.181211511, 176444],
                     ["batch 83 done", 5.234163266, 176592], ["batch 84 done", 5.285682166, 176592],
                     ["batch 85 done", 5.336190634, 176592], ["batch 86 done", 5.386990461, 176792],
                     ["batch 87 done", 5.434720323, 176792], ["batch 88 done", 5.485018141, 176792],
                     ["batch 89 done", 5.53320973, 176792], ["batch 90 done", 5.578538201, 176792],
                     ["batch 91 done", 5.626763489, 176792], ["batch 92 done", 5.674851011, 176792],
                     ["batch 93 done", 5.723934573, 176792], ["batch 94 done", 5.766677618, 176792],
                     ["batch 95 done", 5.808277404, 176792], ["batch 96 done", 5.853653287, 176980],
                     ["batch 97 done", 5.896140664, 176980], ["batch 98 done", 5.947902541, 176980],
                     ["batch 99 done", 5.995292471, 176980], ["batch 100 done", 6.045630902, 177188]],
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
