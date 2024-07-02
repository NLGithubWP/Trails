import matplotlib.pyplot as plt

# Create a figure and axis with the specified size
fig, ax = plt.subplots(figsize=(6.4, 4.5))

# Set the background color to black
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Hide the axes
ax.axis('off')
# Save the figure

plt.tight_layout()
print(f"saving to ./internal/ml/model_slicing/exp_imgs/sql.pdf")
fig.savefig(f"./internal/ml/model_slicing/exp_imgs/sql.pdf", bbox_inches='tight')
