#!/usr/bin/python
# encoding: utf-8

CASOS = [ 
    (['uma'], set(['uma'])),
    (['qual', 'e', 'o', 'doce', 'mais', 'doce'], set(['doce'])),
    (['voce', 'sabe', 'quem', 'sabe', 'sobre', 'voce'], set(['voce', 'sabe'])),
    (['a', 'casa', 'a', 'casa', 'a', 'casa'], set(['a', 'casa'])),
]

def executar_programas(progs, casos):
    for prog in progs:
        print '== Testando programa', prog, '=='
        executar_casos_de_teste(prog, casos)

def executar_casos_de_teste(prog, casos):
    for entrada, saida_esperada in casos:
        executar_caso_de_teste(prog, entrada, saida_esperada)

def executar_caso_de_teste(alg, entrada, saida_esperada):
    saida_obtida = executar_programa(alg, entrada)[1:] # discarta o tempo
    s = set(saida_obtida)
    if len(saida_obtida) != len(s):
        print 'Falha, contém elementos repetidos'
    if s != saida_esperada:
        print 'Falha'
        print '  Esperada:', saida_esperada
        print '  Obtida  :', saida_obtida
        print

def executar_programa(prog, entrada):
    import subprocess
    p = subprocess.Popen(prog.split(' '), stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return p.communicate('\n'.join(entrada))[0].strip().split('\n')

def medir_tempo_programa(prog, entrada, vezes=1):
    tempo_total = 0.0
    for i in range(vezes):
        saida = executar_programa(prog, entrada)
        tempo_total += float(saida[0])
    media = tempo_total / vezes
    return media, saida[1:]

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print u'Modo de usar: %s nome-dos-programas'
        print u'  cada programa deve ler as palavras da entrada padrão e'
        print u'  escrever a resposta na saída padrão'
        print u'  a primeira linha da saída é o tempo de execução do programa'
        sys.exit(0)
    executar_programas(sys.argv[1:], CASOS)
