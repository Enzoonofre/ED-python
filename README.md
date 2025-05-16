# Estruturas de Dados em Python — Pilha, Fila e Lista Encadeada

Este projeto foi desenvolvido com o objetivo de treinar e reforçar os fundamentos de estruturas de dados utilizando Python puro. As implementações incluem **Pilha (Stack)**, **Fila (Queue)** e **Lista Encadeada (Linked List)**, todas feitas com atenção à lógica e à estrutura interna, sem recorrer a bibliotecas externas.

## ⚙️ Estruturas Implementadas

### 🟦 Fila (`Queue`)

Implementada com ponteiros para o primeiro e o último elemento, simulando uma estrutura encadeada.

#### Operações disponíveis:

* `enqueue(valor)` → adiciona um valor ao final da fila.
* `dequeue()` → remove e retorna o valor do início da fila.
* `first_f()` → imprime o valor no início da fila.
* `last_f()` → imprime o valor no final da fila.
* `size()` → imprime o tamanho atual da fila.
* `showQueue()` → exibe visualmente os elementos na ordem da fila.

> A fila segue o padrão **FIFO (First-In, First-Out)**. A implementação trata corretamente casos como fila vazia e atualização dos ponteiros `first` e `last`.

---

### 🟩 Lista Encadeada (`LinkedList`)

Cada elemento (nó) aponta para o próximo, permitindo inserções e remoções flexíveis em qualquer posição da lista.

#### Operações disponíveis:

* `append(valor)` → insere um valor no final da lista.
* `inset_at(idx, valor)` → insere um valor em um índice específico.
* `remove(valor)` → remove o primeiro nó com o valor informado.
* `delete_at(idx)` → remove o valor no índice indicado.
* `print_list()` → exibe os valores da lista com setas (`->`), finalizando com `None`.

> Estrutura ideal para entender manipulação de ponteiros e operações que envolvem varredura da lista. O controle de índices e busca manual reforça o raciocínio algorítmico.

---

### 🟥 Pilha (`Pilha`)

A pilha foi implementada com uma referência ao topo, usando a lógica de inserção e remoção sempre no mesmo ponto.

#### Operações disponíveis:

* `push(valor)` → adiciona um valor no topo da pilha.
* `pop()` → remove o valor do topo.
* `top()` → imprime o valor atual do topo.
* `size()` → imprime o tamanho da pilha.
* `show_stack()` → exibe os elementos do topo até o fundo, simulando a visualização vertical da pilha.

> A estrutura segue o padrão **LIFO (Last-In, First-Out)** e trata com clareza os estados de pilha vazia e empilhamento.


---

## 💡 Objetivo do Projeto

* Consolidar o entendimento de como essas estruturas funcionam por trás dos panos.
* Praticar lógica de ponteiros, controle de fluxo e manipulação manual de memória.
* Servir como base para desafios mais avançados, como construção de árvores, grafos e algoritmos de ordenação.



## ✍️ Autor

Desenvolvido por \Enzo Onofre
[🔗 github.com/Enzoonofre](https://github.com/Enzoonofre)

