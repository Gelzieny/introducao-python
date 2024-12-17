from collections import namedtuple

Caixa = namedtuple('Caixa', 'tem_chave')

def encontra_chave(caixas: list[Caixa], index: int = 0) -> Caixa:
  # Caso base
  if len(caixas) <= index:
    return Caixa(False)
  
  caixa = caixas[index]

  print(f'Busca chave na caixa de índice {index} -> {caixa}')

  # Caso base
  if caixa.tem_chave:
    return caixa
  
  # Caso recursivo
  index += 1
  return encontra_chave(caixas, index)

if __name__ == "__main__":
  caixas: list[Caixa] = [
    Caixa(False), Caixa(True),
    Caixa(False), Caixa(True),
    Caixa(False), Caixa(True),
    Caixa(False), Caixa(True),
    Caixa(False), Caixa(True),
    Caixa(False), Caixa(True),
    Caixa(False), Caixa(True),
    Caixa(False), Caixa(True)
  ]

  print(encontra_chave(caixas))