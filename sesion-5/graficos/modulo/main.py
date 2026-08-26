import matplotlib.pyplot as plt

semanas = [1, 2, 3, 4]
kilometraje = [2, 5, 4, 8]

plt.plot(
    semanas,
    kilometraje,
    color="green",
    marker="o",
    linestyle="--",
    linewidth=2,
    markersize=8,
)

plt.title("Progreso Juan", fontsize=17)
plt.xlabel("semanas", fontsize=14)
plt.ylabel("kilometraje", fontsize=14)

# cuadriculla.
plt.grid(True, linestyle="--", alpha=0.6)

plt.show()