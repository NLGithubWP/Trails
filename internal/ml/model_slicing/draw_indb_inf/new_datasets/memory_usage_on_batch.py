import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Sample data, replace this with your actual data

memory_log = {
    "with all opt": [["batch 1 done",2.536737542,303624],["batch 2 done",2.583939756,303900],["batch 3 done",2.626839595,304076],["batch 4 done",2.66684654,304328],["batch 5 done",2.710223198,304544],["batch 6 done",2.751506876,304636],["batch 7 done",2.789093092,304800],["batch 8 done",2.828705964,304820],["batch 9 done",2.8736365729999997,304976],["batch 10 done",2.9245602269999997,305084],["batch 11 done",2.972938933,305232],["batch 12 done",3.021226329,305368],["batch 13 done",3.065347481,305504],["batch 14 done",3.110408662,305508],["batch 15 done",3.157550182,305656],["batch 16 done",3.21148615,305676],["batch 17 done",3.265599059,305792],["batch 18 done",3.313437168,305792],["batch 19 done",3.3642455079999998,305792],["batch 20 done",3.409141552,305960],["batch 21 done",3.454383603,306112],["batch 22 done",3.4952151479999998,306112],["batch 23 done",3.536616175,306112],["batch 24 done",3.578793348,306112],["batch 25 done",3.62674481,306272],["batch 26 done",3.672992657,306276],["batch 27 done",3.711783349,306276],["batch 28 done",3.755060019,306396],["batch 29 done",3.801803962,306528],["batch 30 done",3.859657021,306760],["batch 31 done",3.907334438,306904],["batch 32 done",3.952439388,307044],["batch 33 done",4.000987401,307044],["batch 34 done",4.048321069,307044],["batch 35 done",4.093785251,307044],["batch 36 done",4.140644382,307044],["batch 37 done",4.1876793469999996,307044],["batch 38 done",4.240831597,308200],["batch 39 done",4.286751487,308280],["batch 40 done",4.324134542,308364],["batch 41 done",4.365593959,308448],["batch 42 done",4.411289154,308448],["batch 43 done",4.456663057,308448],["batch 44 done",4.496621736,308448],["batch 45 done",4.536018539,308448],["batch 46 done",4.577540227,308448],["batch 47 done",4.619472693,308448],["batch 48 done",4.66368263,308464],["batch 49 done",4.714012478,308556],["batch 50 done",4.758426282,308556],["batch 51 done",4.801472301,308556],["batch 52 done",4.901068734,308556],["batch 53 done",4.948471545,308556],["batch 54 done",4.99478452,308604],["batch 55 done",5.043389418,308604],["batch 56 done",5.092407423,308604],["batch 57 done",5.144042341,308604],["batch 58 done",5.195255794,308620],["batch 59 done",5.24643089,308628],["batch 60 done",5.298451583,308628],["batch 61 done",5.345737299,308732],["batch 62 done",5.3962836880000005,308732],["batch 63 done",5.4469368320000005,308756],["batch 64 done",5.499042263,308756],["batch 65 done",5.548965467,308756],["batch 66 done",5.595175591,308756],["batch 67 done",5.637410171,308756],["batch 68 done",5.689742926,308784],["batch 69 done",5.738156511,308784],["batch 70 done",5.781054171,308784],["batch 71 done",5.832948697,308880],["batch 72 done",5.879774644,309004],["batch 73 done",5.925833783,309020],["batch 74 done",5.9722614830000005,309020],["batch 75 done",6.020639769,309116],["batch 76 done",6.072403068,309116],["batch 77 done",6.116614287,309128],["batch 78 done",6.159717142,309140],["batch 79 done",6.202310378,309140],["batch 80 done",6.246358933,309140],["batch 81 done",6.292526404,309140],["batch 82 done",6.339772662,309160],["batch 83 done",6.389652476,309188],["batch 84 done",6.436281875,309188],["batch 85 done",6.487691529,309188],["batch 86 done",6.531846964,312176],["batch 87 done",6.57341219,312192],["batch 88 done",6.614329806,312200],["batch 89 done",6.653774147,312200],["batch 90 done",6.6960414539999995,312280],["batch 91 done",6.73522412,312316],["batch 92 done",6.776151219,312336],["batch 93 done",6.824820348,312348],["batch 94 done",6.87071352,312440],["batch 95 done",6.914404996,312440],["batch 96 done",6.954861219,312444],["batch 97 done",7.001335399,312452],["batch 98 done",7.04048903,312452],["batch 99 done",7.079479726,312452],["batch 100 done",7.123081074,312452]],
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
