#include <iostream>
#include <fstream>
#include <sstream>
#include <list>
#include <unordered_map>
#include <string>
#include <ctime>
#include <cstdlib>

using namespace std;

struct Frequencia {
    string palavra;
    int freq;
};

list<Frequencia> alg_a(list<string> palavras) {
    list<Frequencia> freqs;
    int max_freq = 0;
    
    for (list<string>::iterator i = palavras.begin(); i != palavras.end(); i++) {
        int freq = 0;
        for(list<string>::iterator j = palavras.begin(); j != palavras.end(); j++) {
            if(*j == *i){
                freq++;
            }
        }
        
        if (freq == max_freq) {
            bool tem_freq = false;
            for (auto &freq_palavra : freqs) {
                if(freq_palavra.palavra == *i){
                    tem_freq = true;
                }
            }
            if (!tem_freq){
                Frequencia freq_palavra;
                freq_palavra.palavra = *i;
                freq_palavra.freq = freq;
                freqs.push_back(freq_palavra);
            }
        } else if (freq > max_freq) {
            max_freq = freq;
            freqs.clear();
            Frequencia freq_palavra;
            freq_palavra.palavra = *i;
            freq_palavra.freq = freq;
            freqs.push_back(freq_palavra);
        }
    }
    
    return freqs;
}

list<Frequencia> alg_b(list<string> palavras) {
    list<Frequencia> freqs;
    int max_freq = 0;
    
    for (list<string>::iterator i = palavras.begin(); i != palavras.end(); i++) {
        int freq = 0;
        for(list<string>::iterator j = i; j != palavras.end(); j++) {
            if(*j == *i){
                freq++;
            }
        }

        if (freq == max_freq) {
            Frequencia freq_palavra;
            freq_palavra.palavra = *i;
            freq_palavra.freq = freq;
            freqs.push_back(freq_palavra);
        } else if (freq > max_freq) {
            max_freq = freq;
            freqs.clear();
            Frequencia freq_palavra;
            freq_palavra.palavra = *i;
            freq_palavra.freq = freq;
            freqs.push_back(freq_palavra);
        }
    }
    
    return freqs;
}

list<Frequencia> alg_c(list<string> palavras) {
    list<Frequencia> freqs;
    int max_freq = 0;
    
    palavras.sort();
    
    list<string>::iterator i = palavras.begin();
    list<string>::iterator fim = palavras.end();
    
    while (i != fim) { 
        list<string>::iterator j = i;
        j++;
        
        int freq = 1;
        while (j != fim && *j == *i) {
            freq++;
            j++;
        }
        
        if (freq == max_freq) {
            Frequencia freq_palavra;
            freq_palavra.palavra = *i;
            freq_palavra.freq = freq;
            freqs.push_back(freq_palavra);
        } else if (freq > max_freq) {
            max_freq = freq;
            freqs.clear();
            Frequencia freq_palavra;
            freq_palavra.palavra = *i;
            freq_palavra.freq = freq;
            freqs.push_back(freq_palavra);
        }
        
        i = j;
    }
    
    return freqs;
}

list<Frequencia> alg_d(list<string> palavras) {
    list<Frequencia> freqs;
    unordered_map<string, int> freqs_hash;
    freqs_hash.reserve(palavras.size());
    int max_freq = 0;
    
    for (auto &palavra : palavras) {
        freqs_hash[palavra]++;
        int freq = freqs_hash[palavra];
        
        if (freq == max_freq) {
            Frequencia freq_palavra;
            freq_palavra.palavra = palavra;
            freq_palavra.freq = freq;
            freqs.push_back(freq_palavra);
        } else if (freq > max_freq) {
            max_freq = freq;
            freqs.clear();
            Frequencia freq_palavra;
            freq_palavra.palavra = palavra;
            freq_palavra.freq = freq;
            freqs.push_back(freq_palavra);
        }
    }
    
    return freqs;
}

void print(list<string> palavras) {
    cout << "(palavra):" << "\n";
    for (auto &palavra : palavras) {
        cout << "(" << palavra << ")" << "\n";
    }
}

void print(list<Frequencia> freqs) {
    cout << "(palavra, frequencia):" << "\n";
    for (auto &freq : freqs) {
        cout << "(" << freq.palavra << "," << freq.freq << ")" << "\n";
    }
}

void print_palavras(list<Frequencia> freqs){
    for(auto &freq : freqs){
        cout << freq.palavra << endl;
    }
}

void read_text_file(const char *filename, list<string>& v) {
    ifstream fin(filename);
    istream *in;
    if (string("-") == filename) {
        in = &cin;
    } else {
        in = &fin;
    }
    if (in->fail()) {
        cout << "Não foi possivél abrir o arquivo: " << filename << endl;
        exit(0);
    }
    string s;
    while (getline(*in, s)) {
        v.push_back(s);
    }
}

int str2int(string s) {
    istringstream buffer(s);
    int i;
    buffer >> i;
    return i;
}

void show_usage(const char* argv[]) {
    cout << "Modo de usar: " << argv[0] << " algoritmo [arquivo]" << endl;
    cout << "    algoritmo é um dos valores:" << endl;
    cout << "        a - for aninhado " <<  endl;
    cout << "        b - for aninhado com j = i + 1" << endl;
    cout << "        c - ordenando a entrada" << endl;
    cout << "        d - tabela hash" << endl;
    cout << "    arquivo é o nome de um arquivo com uma palavra por linha" << endl;
    cout << "        se o nome do arquivo não for informado, a entrada" << endl;
    cout << "        padrão é utilizada" << endl;
}

int main(int argc, const char* argv[]) {
    if (argc != 2 && argc != 3) {
        show_usage(argv);
        return 0;
    }

    // parametro algoritmo
    string alg_name = argv[1];
    list<Frequencia> (*alg)(list<string>);

    if (alg_name == "a") {
        alg = alg_a;
    } else if (alg_name == "b") {
        alg = alg_b;
    } else if (alg_name == "c") {
        alg = alg_c;
    } else if (alg_name == "d") {
        alg = alg_d;
    } else {
        cout << "Nome do algoritmo inválido: " << alg_name << endl;
        show_usage(argv);
        return 1;
    }
        
    // parametro arquivo
    const char *filename = argc == 2 ? "-" : argv[2];
    list<string> palavras;
    read_text_file(filename, palavras);

    // executa o algoritmo
    clock_t start = clock();
    list<Frequencia> saida = alg(palavras);
    double tempo = (double)(clock() - start) / CLOCKS_PER_SEC;
    cout << tempo << endl << flush;

    // imprime a saida
    print_palavras(saida);
    return 0;
}
