import matplotlib.pyplot as plt

edades = [20, 22, 21, 25, 30, 35, 18, 19, 40, 45, 22, 23, 21]

plt.hist(edades, bins=5, color="blue", edgecolor="black")

plt.title("Distribución de edades en el cine")
plt.xlabel("Edad")
plt.ylabel("Número de personas")

plt.show()
