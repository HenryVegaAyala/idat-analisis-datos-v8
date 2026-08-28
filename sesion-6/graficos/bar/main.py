import matplotlib.pyplot as plt

animales = ["Perro", "Gato", "Aves", "Peces"]
cantidad = [45, 38, 12, 5]

plt.bar(animales, cantidad, color=["red", "green", "blue", "yellow"])

plt.title("Mascotas favoritas", fontsize=20)
plt.xlabel("Mascotas", fontsize=15)
plt.ylabel("Cantidad", fontsize=15)

plt.grid(True, linestyle="--", alpha=0.6)

plt.show()