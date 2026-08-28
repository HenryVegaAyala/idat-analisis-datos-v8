import matplotlib.pyplot as plt

edades = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 50]

plt.hist(edades, bins=5, color="skyblue", edgecolor="black")

plt.show()