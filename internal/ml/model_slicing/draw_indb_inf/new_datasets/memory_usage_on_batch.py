import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Sample data, replace this with your actual data

memory_log = {
    "with all opt": [["batch 1 done", 1.071418596, 172420], ["batch 2 done", 1.120360142, 172680],
                      ["batch 3 done", 1.167287062, 172680], ["batch 4 done", 1.215315636, 172680],
                      ["batch 5 done", 1.2634362270000001, 173048], ["batch 6 done", 1.311735845, 173056],
                      ["batch 7 done", 1.355895208, 173056], ["batch 8 done", 1.402644186, 173056],
                      ["batch 9 done", 1.452793433, 173088], ["batch 10 done", 1.499623696, 173284],
                      ["batch 11 done", 1.5496507130000001, 173440], ["batch 12 done", 1.6050429080000002, 173440],
                      ["batch 13 done", 1.655168072, 173632], ["batch 14 done", 1.699802413, 173632],
                      ["batch 15 done", 1.751876589, 173632], ["batch 16 done", 1.80647215, 173632],
                      ["batch 17 done", 1.8604224280000001, 173812], ["batch 18 done", 1.909897733, 173812],
                      ["batch 19 done", 1.958091482, 174000], ["batch 20 done", 2.012890978, 174000],
                      ["batch 21 done", 2.061702051, 174188], ["batch 22 done", 2.110257317, 174384],
                      ["batch 23 done", 2.158949123, 174384], ["batch 24 done", 2.211920261, 174384],
                      ["batch 25 done", 2.262675128, 174384], ["batch 26 done", 2.314783708, 174384],
                      ["batch 27 done", 2.363550931, 174384], ["batch 28 done", 2.411228293, 174384],
                      ["batch 29 done", 2.466272712, 174576], ["batch 30 done", 2.512883695, 174576],
                      ["batch 31 done", 2.567873685, 174576], ["batch 32 done", 2.613249202, 174576],
                      ["batch 33 done", 2.665830872, 174768], ["batch 34 done", 2.7183963330000003, 174768],
                      ["batch 35 done", 2.771060082, 174768], ["batch 36 done", 2.815967498, 174768],
                      ["batch 37 done", 2.86400182, 174956], ["batch 38 done", 2.914447839, 174956],
                      ["batch 39 done", 2.961345575, 175140], ["batch 40 done", 3.011495759, 175140],
                      ["batch 41 done", 3.061494851, 175140], ["batch 42 done", 3.116229097, 175140],
                      ["batch 43 done", 3.1685577990000002, 175140], ["batch 44 done", 3.218691701, 175324],
                      ["batch 45 done", 3.262427068, 175324], ["batch 46 done", 3.3139642, 175472],
                      ["batch 47 done", 3.366308934, 175648], ["batch 48 done", 3.420310513, 175820],
                      ["batch 49 done", 3.470608468, 175820], ["batch 50 done", 3.516802164, 175820],
                      ["batch 51 done", 3.564929961, 175820], ["batch 52 done", 3.614748162, 176012],
                      ["batch 53 done", 3.66850811, 176012], ["batch 54 done", 3.720563339, 176012],
                      ["batch 55 done", 3.76954805, 176196], ["batch 56 done", 3.822337997, 176196],
                      ["batch 57 done", 3.871841211, 176196], ["batch 58 done", 3.918895691, 176196],
                      ["batch 59 done", 3.965611165, 176196], ["batch 60 done", 4.016748558, 176196],
                      ["batch 61 done", 4.065384638, 176196], ["batch 62 done", 4.112533942, 176196],
                      ["batch 63 done", 4.162012416, 176196], ["batch 64 done", 4.211918985, 176196],
                      ["batch 65 done", 4.264137337, 176196], ["batch 66 done", 4.312633155, 176196],
                      ["batch 67 done", 4.366797756, 176196], ["batch 68 done", 4.41518501, 176196],
                      ["batch 69 done", 4.462881595, 176196], ["batch 70 done", 4.513740382, 176196],
                      ["batch 71 done", 4.565994852, 176196], ["batch 72 done", 4.616556844, 176196],
                      ["batch 73 done", 4.66771212, 176196], ["batch 74 done", 4.718983439, 176196],
                      ["batch 75 done", 4.77075719, 176384], ["batch 76 done", 4.819358531, 176384],
                      ["batch 77 done", 4.867544842, 176384], ["batch 78 done", 4.915480663, 176384],
                      ["batch 79 done", 4.968917336, 176384], ["batch 80 done", 5.01895277, 176384],
                      ["batch 81 done", 5.072878035, 176576], ["batch 82 done", 5.122550446, 176576],
                      ["batch 83 done", 5.177176217, 176576], ["batch 84 done", 5.226293566, 176576],
                      ["batch 85 done", 5.275222401, 176764], ["batch 86 done", 5.324822023, 177056],
                      ["batch 87 done", 5.374297766, 177056], ["batch 88 done", 5.425408531, 177252],
                      ["batch 89 done", 5.476977411, 177252], ["batch 90 done", 5.533562652, 177252],
                      ["batch 91 done", 5.586147914, 177448], ["batch 92 done", 5.636493708, 177448],
                      ["batch 93 done", 5.688866976, 177448], ["batch 94 done", 5.734429595, 177448],
                      ["batch 95 done", 5.786275362, 177448], ["batch 96 done", 5.838742449, 177448],
                      ["batch 97 done", 5.890164622, 177448], ["batch 98 done", 5.940368949, 177448],
                      ["batch 99 done", 5.990953202, 177448], ["batch 100 done", 6.04539901, 177448]],
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
