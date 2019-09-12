#!/usr/bin/python
# encoding: utf-8

def gerar_palavras(count):
    palavras = [None] * count
    for i in range(count):
        palavras[i] = gerar_palavra()
    return palavras

def gerar_palavra(min_silabas = 1, max_silabas = 3):
    import random
    num_silabas = random.randint(min_silabas, max_silabas)
    palavra = ''
    for i in range(num_silabas):
        palavra += random.choice('bcdfghjklmnpqrstvxyz')
        palavra += random.choice('aeiou')
    return palavra

def showUsage(argv):
    print u"Este programa gerar palavras aleatórias."
    print u"Modo de usar: %s numero-de-palavras" % argv[0]

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        showUsage(sys.argv)
        sys.exit(0)

    try:
        palavras = gerar_palavras(int(sys.argv[1]))
        for p in palavras:
            print p
    except ValueError:
        showUsage(sys.argv)
