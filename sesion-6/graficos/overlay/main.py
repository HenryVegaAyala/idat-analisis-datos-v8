import matplotlib.pyplot as plt
from openpyxl.chart import label, marker

# datos del mes
mes = ["Enero", "Febrero", "Marzo", "Abril"]

# gastos mensualkes de cada servicio en soles
luz = [40, 50, 56, 60]
agua = [25, 30, 31, 35]

# Crear grafico de gastos de luz
plt.plot(
    mes,
    luz,
    label="Servicio de luz",
    marker="o",
    linewidth=3,
    color="blue"
)

# Crear grafico de gastos de agua
plt.plot(
    mes,
    agua,
    label="Servicio de agua",
    marker="s",
    linewidth=3,
    color="red"
)

plt.grid(True)
plt.legend()

plt.title("Gastos de la casa")
plt.xlabel("Mes")
plt.ylabel("Gastos S/.")

plt.show()
