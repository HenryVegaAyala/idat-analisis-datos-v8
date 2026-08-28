import matplotlib.pyplot as plt
from PIL.ImageOps import scale
from openpyxl.chart import label, marker

# datos del mes
mes = ["Enero", "Febrero", "Marzo", "Abril"]

# gastos mensualkes de cada servicio en soles
luz = [40, 50, 56, 60]
agua = [25, 30, 31, 35]

# Crear grafico de gastos de luz
plt.bar(
    mes,
    luz,
    label="Servicio de luz",
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

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.title("Gastos de la casa")
plt.xlabel("Mes")
plt.ylabel("Gastos S/.")

plt.savefig("Gastos_de_la_cine.png")
