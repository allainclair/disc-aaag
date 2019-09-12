test: contagem contagem-o3 contagem.py
	@for alg in a b c d; do ./testador.py "./contagem $$alg"; done
	@for alg in a b c d; do ./testador.py "./contagem-o3 $$alg"; done
	@for alg in a b c d; do ./testador.py "./contagem.py $$alg"; done

comparar-alg-a-b-cpp: contagem
	./comparador.py 1000 5000 400 10 './contagem a' './contagem b'

comparar-alg-a-c-cpp: contagem
	./comparador.py 10000 50000 4000 10 './contagem a' './contagem c'

comparar-alg-a-b-python: contagem.py
	./comparador.py 1000 5000 400 10 './contagem.py a' './contagem.py b'

comparar-alg-a-c-python: contagem.py
	./comparador.py 10000 50000 4000 10 './contagem.py a' './contagem.py c'

comparar-alg-a-python-a-cpp: contagem
	./comparador.py 1000 5000 400 10 './contagem.py a' './contagem a'

comparar-alg-c-d-python: contagem.py
	./comparador.py 100000 200000 10000 1 './contagem.py c' './contagem.py d'

comparar-alg-c-d-cpp: contagem
	./comparador.py 100000 200000 10000 10 './contagem c' './contagem d'

comparar-alg-c-python-c-cpp: contagem
	./comparador.py 100000 200000 10000 10 './contagem.py c' './contagem c'

comparar-alg-c-cpp-c-cppo3: contagem contagem-o3
	./comparador.py 100000 200000 10000 10 './contagem c' './contagem-o3 c'

comparar-alg-d-cpp-d-cppo3: contagem contagem-o3
	./comparador.py 100000 200000 10000 10 './contagem d' './contagem-o3 d'

comparar-alg-d-python-d-cpp: contagem
	./comparador.py 100000 200000 10000 10 './contagem.py d' './contagem d'

contagem: contagem.cpp
	g++ -std=c++0x contagem.cpp -o contagem

contagem-o3: contagem.cpp
	g++ -O3 -std=c++0x contagem.cpp -o contagem-o3

clean:
	rm -f contagem contagem-o3 *.pyc contagem.zip

zip:
	make clean
	zip contagem.zip -r .
