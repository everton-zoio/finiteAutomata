 # finiteAutomata

#### Execução:

O Projeto conta com exemplos de autômatos finitos para teste, para executar um teste, basta fazer como na instrução a baixo:
```sh
$ python3 FiniteAuto.py automatos/ex1.1a.jff.txt aabb
```
###### Onde:
- "FiniteAuto.py" é o algoritmo de simulação do autômato finito;
- "automatos/ex1.1a.jff.txt" é o formato de trabalho;
- "aabb" é um exemplo de palavra de entrada;

#### Funcionamento de Código:
O programa lê o arquivo e distribui os dados dentre os atributos, a partir daí são gerados os estados de acordo com a terceira linha do arquivo de entrada, assim como as transições, que são distribuidas entre os estados.

Como o python aceita caracteres com aspas vazias (''), foi utilizado uma equivalência para o epsilon, colocando ('') no lugar do mesmo.

O algoritmo conta com 4 classes :
- Automato: Classe implementada para simular a configuração instantânea do autômato;
- Fita:  Classe implementada para simular a fita de entrada e a pilha do autômato;
- Estado: Corresponde aos estados do autômato;
- Transicao: Representa as transições de cada estado.


A classe Automato possui os atributos:
- Entrada (classe Fita), onde será recebida a palavra de entrada;
- Estado (classe Estado), representando o estado atual do autômato, começa apontando para o estado inicial e alterna entre os demais estados de acordo com a validação das transições de cada estado.

A função main conta com dois laços de repetição principais, o laço de fora itera até que um resultado seja encontrado, já o laço de dentro trata de executar todos os autômatos (se necessário duplicá-los), pois após toda validação de transições, verifica-se se há mais de uma transição válida, caso houver, um vetor com o índice dessas transições é criado e o autômato é copiado conforme o número de transições válidas (apenas se houver mais de uma) e suas cópias inseridas no vetor de autômatos.

O algoritmo retorna:
- 0 caso a palavra de entrada seja aceita, e mostra a descrição instantânea
- 1 caso a palavra de entrada for rejeitada, e mostra a descrição instantânea
- Apenas mostra a descrição instantânea caso o autômato for interrompido
### Desenvolvedores

    Everton Junior de Abreu
    Lucas Daniel Deolindo dos Santos
    Lucas Souza Santos

Licença
----

MIT