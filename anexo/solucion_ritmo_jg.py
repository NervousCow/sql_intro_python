# SOLUCION DESAFIO RITMO CARDIACO

import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def fetch():
    conn = sqlite3.connect('heart.db')
    c = conn.cursor()
    c.execute("""
        SELECT pulso FROM sensor;
    """)
    pulsos = c.fetchall()

    return pulsos

def show(data):

    x = range(len(data))
    y = data

    fig = plt.figure()
    fig.suptitle('Pulsaciones durante un partido de futbol', fontsize=16)
    ax = fig.add_subplot()

    ax.plot(x, y, c='darkgreen', lw=1.5, label='Pulso')
    ax.set_facecolor('whitesmoke')
    ax.legend()
    ax.grid()

    plt.show()

def estadistica(data):

    valor_medio = np.mean(data)
    #print(f'Pulso promedio {valor_medio}')
    
    valor_min = np.min(data)
    #print(f'Pulso mínimo {valor_min}')

    valor_max = np.max(data)
    #print(f'Pulso máximo {valor_max}')

    valor_std = np.std(data)
    #print(f'El desvio estandar para las pulsasiones medidas es {valor_std}')

    return valor_medio, valor_min, valor_max, valor_std

def regiones(data, valor_medio, valor_std):

    #Pulso menor o igual al promedio
    x1 = []
    y1 = []

    # Pulso mayor o igual al promedio
    x2 = []
    y2 = []

    # Pulso que no entra en las cosndiciones anteriores
    x3 = []
    y3 = []


    for i in range(len(data)):
        if data[i] <= (valor_medio-valor_std):
            x1.append(i)
            y1.append(data[i])
        elif data[i] >= (valor_medio+valor_std):
            x2.append(i)
            y2.append(data[i])
        else:
            x3.append(i)
            y3.append(data[i])

    
    fig = plt.figure()
    fig.suptitle('EMOCIONES SEGÚN PULSO')
    ax = fig.add_subplot()

    ax.scatter(x1, y1, c='blue', marker='*', label='Aburrido')
    ax.scatter(x2, y2, c='yellow', marker='^', label='Divertido')
    ax.scatter(x3, y3, c='black', marker='.', label='Normal')
    ax.set_facecolor('whitesmoke')
    ax.legend()
    ax.grid()

    plt.show()




if __name__ == "__main__":
    # La DATA
    data = fetch()

    # El analisis...
    show(data)
    valor_medio, valor_min, valor_max, valor_std = estadistica(data)
    regiones(data, valor_medio, valor_std)

    print('Terminamos')