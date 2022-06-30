## O Problema do Caixeiro Viajante - Traveling Salesman Problem (TSP)

Este problema consiste na determinação do percurso pelo caixeiro, passando por todas as cidades em seu território exatamente uma vez e retornando à origem, de forma a cobrir a menor distância, dado que o custo entre os pares de cidade é conhecido.

O problema do caixeiro viajante é o problema NP-completo mais notório. Isto em função tanto de sua utilidade geral quanto da facilidade com que pode ser explicado ao público em geral. Imagine um caixeiro viajante planejando uma viagem de carro para visitar um conjunto de cidades. Qual é o percurso mais curto que lhe permitirá fazer isso e voltar para casa, minimizando assim sua rota total? O problema do caixeiro viajante surge em muitos problemas de transporte e rota. Outras aplicações importantes envolvem a otimização de caminhos de ferramentas para equipamentos industriais.

A entrada para execução dos testes será um arquivo contendo um grafo completo,
cujos vértices são dados por um conjunto de coordenadas cartesianas. O peso nas arestas
corresponde à distância euclidiana. 

Os arquivos de entrada serão fornecidos no formato de uma lista de vértices.
Os dados dos arquivos estão no formato:

```
identificador_do_nó coordenada_x coordenada_y
```

### Execução

```
pip install numpy
```

```
python3 <algoritmo>/<algoritmo>.py inputs/<input>.tsp.txt
```