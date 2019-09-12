#!/usr/bin/python
# encoding: utf-8

# for aninhado
def alg_a(palavras):
    saida = set()
    max_freq = 0
    for i in range(len(palavras)):
        freq = 0
        for j in range(len(palavras)):
            if palavras[i] == palavras[j]:
                freq += 1
            j += 1

        if freq == max_freq:
            saida.add(palavras[i])
        elif freq > max_freq:
            saida = set([palavras[i]])
            max_freq = freq

        i += 1
    return saida

# for aninhado onde j = i + 1
def alg_b(palavras):
    saida = set()
    max_freq = 0
    for i in range(len(palavras)):
        freq = 1
        for j in range(i + 1, len(palavras)):
            if palavras[i] == palavras[j]:
                freq += 1
            j += 1

        if freq == max_freq:
            saida.add(palavras[i])
        elif freq > max_freq:
            saida = set([palavras[i]])
            max_freq = freq

        i += 1
    return saida

# ordena e conta o tamanho da sequência com elementos repetidos
def alg_c(palavras):
    saida = set()
    palavras.sort()
    max_freq = 0
    i = 0
    while i < len(palavras):
        j = i + 1
        freq = 1
        while j < len(palavras) and palavras[i] == palavras[j]:
            freq += 1
            j += 1

        if freq == max_freq:
            saida.add(palavras[i])
        elif freq > max_freq:
            saida = set([palavras[i]])
            max_freq = freq

        i = j
    return saida

# usando tabela hash
def alg_d(palavras):
    saida = set()
    freq_hash = {}
    max_freq = 0
    for i in range(len(palavras)):
        if palavras[i] in freq_hash:
            freq_hash[palavras[i]] += 1
            freq = freq_hash[palavras[i]]
        else:
            freq_hash[palavras[i]] = 1
            freq = 1

        if freq == max_freq:
            saida.add(palavras[i])
        elif freq > max_freq:
            saida = set([palavras[i]])
            max_freq = freq

    return saida


def show_usage(argv):
    print 'Modo de usar: %s algorimo [arquivo]' % argv[0]
    print "    algoritmo é um dos valores:"
    print "        a - for aninhado "
    print "        b - for aninhado com j = i + 1"
    print "        c - ordenando a entrada"
    print "        d - tabela hash"
    print "    arquivo é o nome de um arquivo com uma palavra por linha"
    print "        se o nome do arquivo não for informado, a entrada"
    print "        padrão é utilizada"
        
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        show_usage(sys.argv)
        sys.exit(0)

    # parametro algoritmo
    alg_name = sys.argv[1]
    if alg_name == 'a':
        alg = alg_a
    elif alg_name == 'b':
        alg = alg_b
    elif alg_name == 'c':
        alg = alg_c
    elif alg_name == 'd':
        alg = alg_d
    else:
        print u'Nome do algoritmo inválido:', alg_name
        show_usage(sys.argv)
        sys.exit(0)

    # le a entrada
    filename = "-" if len(sys.argv) == 2 else sys.argv[2]
    if filename == "-":
        f = sys.stdin
    else:
        f = open(filename)
    palavras = [ s.strip() for s in f ]
    f.close()

    # executa o algoritmo
    import time
    start = time.clock()
    saida = alg(palavras)
    tempo = time.clock() - start

    # imprime a saída
    print tempo
    for p in saida:
        print p
