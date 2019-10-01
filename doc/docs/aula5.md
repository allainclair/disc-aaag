## Técnica de projeto: Divisão e Conquista

  * Dividir o problema em um número de subproblemas;

  * Conquistar os subproblemas resolvendo-os recursivamente;

    * Caso base: se os subproblemas forem suficientemente pequenos,
      resolvê-los de maneira direta.

  *  Combinar as soluções dos subproblemas para obter a solução
     do problema original.

Exemplo de aplicação de Divisão e Conquista
Problema de ordenação, algoritmo Mergesort.


## Análise de complexidade de algoritmos de divisão e conquista

Uso de equação de recorrência.

T(n) = c  caso base

T(n) = aT(n/b) + D(n) + C(n) caso contrário

* T(n) representa o tempo de execução de um problema de
tamanho n.

* a: quantidade de subproblemas;

* 1/b: tamanho do subproblema;

* D(n): tempo para dividir o problema;

* C(n): tempo para combinar as soluções.
