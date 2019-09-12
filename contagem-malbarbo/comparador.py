#!/usr/bin/python
# encoding: utf-8

from gerador_de_palavras import *
from testador import *

import matplotlib.pyplot as plt
def executar(inicial, final, passo, vezes, programas):
    executar_programas(programas, CASOS)

    tamanhos = [t for t in range(inicial, final, passo)]

    tempos = [[] for i in programas]

    plt.ion()
    for t in range(len(tamanhos)):
        plt.clf()
        plt.xlim(tamanhos[0], tamanhos[-1])
        tamanho = tamanhos[t]
        print 'Tamanho', tamanho
        palavras = gerar_palavras(tamanho)
        for i in range(len(programas)):
            print 'Programa', programas[i]
            tempo, saida = medir_tempo_programa(programas[i], palavras, vezes)
            tempos[i].append(tempo)
            print saida
        for i in range(len(programas)):
            plt.plot(tamanhos[:t+1], tempos[i])
            plt.draw()
        print


    for j in range(len(tamanhos)):
        print "%8d" % tamanhos[j],
        for i in range(len(programas)):        
            print '%6.02f' % tempos[i][j],
        print

    plt.ioff()
    plt.show()

def show_usage(argv):
    print 'Modo de usar: %s tamanho-inicial tamanho-final passo repeticao programas' % argv[0]
    print '    tamanho-inicial quantidade de palavras para o primero caso'
    print '    tamanho-final   quantidade máxima de palavras para o último caso'
    print '    passo           quantidade de palvras que aumenta em cada caso'
    print '    vezes           quantidade de vezes que cada algoritmo é executado' 
    print '    programas       programas a serem executados'    

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 6:
        show_usage(sys.argv)
        sys.exit(0)

    try:
        inicial = int(sys.argv[1])
        final = int(sys.argv[2])
        passo = int(sys.argv[3])
        vezes = int(sys.argv[4])
        programas = sys.argv[5:]
    except ValueError:
        show_usage(sys.argv)
        sys.exit(1)

    executar(inicial, final, passo, vezes, programas)
