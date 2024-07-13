import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Sample data, replace this with your actual data
memory_log = {
    "with all opt": [[0.012600245, 18748], [1.043574622, 181904], [2.880909715, 439356], [4.746978433, 450032],
                     [6.580087388, 454812], [8.395959081, 461368], [10.229162885, 466332], [12.037321584, 470420],
                     [13.867830914, 479540], [15.682375319, 481492], [17.114590375, 489424], [18.88665319, 487128],
                     [20.715824796, 493432], [22.523327161, 498308], [24.340567323, 510192], [26.164078111, 509144],
                     [27.992991493, 510196], [29.810057809, 516004], [31.624005968, 529172], [33.433013773, 531936],
                     [35.25928479, 532344], [37.092092925, 538364], [38.102963907, 548744],
                     [39.924327023000004, 545516], [41.729301603, 550884], [43.540291392, 557808],
                     [45.347360579, 561724], [47.169496446, 556168], [49.011585526, 581232], [50.823214165, 574888],
                     [52.64347461, 573316], [54.447590065, 571784], [56.276114357, 578064], [57.283435147, 570924],
                     [59.12331606, 576356], [60.942781559, 577336], [62.764237568, 581372], [64.595277978, 575348],
                     [66.403776621, 574876], [68.20959977, 578288], [70.019599508, 574892], [71.859492037, 567136],
                     [73.663600443, 567480], [75.487515269, 576564], [77.133634976, 567664], [78.954270747, 578108],
                     [80.79577953, 577728], [82.635105627, 575796], [84.447651732, 571864], [86.268515464, 578308],
                     [88.083857798, 575500], [89.922615099, 567136], [91.729333261, 574744]],
    # "w/o state cache": [],
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
