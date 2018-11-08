# finiteAutomata

#### Execução:

O Projeto conta com exemplos de autômatos finitos para teste, para executar basta:
```sh
$ python3 FiniteAuto.py automatos/ex1.1a.jff.txt aabb
```
##### Onde:
- "FiniteAuto.py" é o algoritmo de simulação do autômato finito;
- "automatos/ex1.1a.jff.txt" é o formato de trabalho;
- "aabb" é um exemplo de palavra de entrada;

#### Funcionamento de Código:
O programa lê o arquivo e distribui os dados dentre os atributos, a partir dai são gerados os estados de acordo com a terceira linha do arquivo de entrada, então as transições de cada estado são gerados

Como o python aceita caracteres com aspas vazias (''), foi utilizado uma equivalencia para o epsilon, colocando ('') no lugar do mesmo.

### Desenvolvedores

    Everton Junior de Abreu
    Lucas Daniel Deolindo dos Santos
    Lucas Souza Santos

Licença
----

MIT

