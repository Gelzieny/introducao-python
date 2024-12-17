"""
Podemos usar listas para representar pilhas em Python já que só precisamos dos
métodos append, para adicionar itens ao topo da pilha, e pop, para remover
itens do topo da pilha.

Exemplos abaixo são apenas para append e pop
"""

# Criando a pilha vazia
stack: list[str] = []

# Adicionando elementos ao topo da pilha
stack.append('A')
stack.append('B')
stack.append('C')

# Removendo elementos do topo da pilha
top_item = stack.pop()  # C
top_item = stack.pop()  # B
top_item = stack.pop()  # A

print(stack, top_item)