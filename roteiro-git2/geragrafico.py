import numpy as np
import matplotlib.pyplot as plt

from leitorarquivo import LeitorArquivo
 
def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    print(valores)

    plt.plot(valores)
    plt.show()

    
    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')

    plt.title('Gráfico de linhas')

    for serie in valores:
   plt.plot(serie, label='Série ' + str(i))

main()

