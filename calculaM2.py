import numpy as np
import matplotlib.pyplot as plt
import math

def calcularM2(atrito = 0.0, massa1 = 5, angulo = 60.0):
    return atrito*massa1*math.tan(math.radians(angulo))

#Definindo intervalo de valores para o coeficiente de atrito
atrito = np.linspace(0,5)
massa2 = [calcularM2(a) for a in atrito]

plt.plot(atrito, calcularM2(atrito))
plt.title('Gráfico Massa 2 (em kg) x Coeficiente de atrito')
plt.ylim(0, max(massa2))
plt.xlim(0, 5)
plt.xticks(np.arange(0, 5.5, 0.5))
plt.yticks(np.arange(0, calcularM2(5), 1))
plt.grid()
plt.show()




