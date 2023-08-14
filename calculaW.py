import numpy as np
import matplotlib.pyplot as plt
import math

"""Solução geral para o problema:
    - Considera-se que todas as forças são perpendiculares ao braço
    - Considera-se que o campo de forças w.d está na extremidade do braço"""

def somaMomento(forcas):
    total = 0
    for par in forcas:
      total += par[0]*par[1]
    return total
def calculaW(d, *forcasM):
    #d -> comprimento do campo
    #*forcasM -> todas as forças perpendiculares com suas distâncias
    return (-(somaMomento(forcasM))/(3*d - d**2/2))

distancias = np.linspace(0,4)
cjtW = [calculaW(d, [37.5, 0.25], [-300, 2]) for d in distancias]
plt.plot(distancias, cjtW)
plt.title('Gráfico Carga W (em N/m) x Comprimento de carga(em metro)')
plt.grid()
plt.show()