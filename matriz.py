
def leitor(matriz, linha, coluna):
  for l in range(linha):
    for col in range(coluna):
      dado = int(input('value: '))
      matriz[l][col] = dado
  return matriz


def calculador_soma_coluna(matriz):
  vetor_soma = []

  for cols in matriz:
    vetor_soma.append(sum(cols))
  return vetor_soma


def calculador_transposta(matriz):
  linha = len(matriz[0])
  coluna = len(matriz)
  matriz_transposta = [[0 for x in range(coluna)] for x in range(linha)]

  for index, i in enumerate(range(linha)):
    l = []
    for line in matriz:
      l.append(line[index])
    matriz_transposta[i] = l
    
  return matriz_transposta
    
def imprimir(matriz):
  for line in matriz:
    for col in line:
      print(col, end=' ')
    print('')

def matriz_triangular(matriz):
  triangular = []
  for i, column in enumerate(matriz):
    if i != 0:
      triangular += [x for x in column[:i]]
  return triangular
    
  
def main():
  linha = int(input('Tamanho de linha: '))
  coluna = int(input('Tamanho de coluna: '))
  matriz = [[0 for x in range(coluna)] for j in range(linha)]
  matriz = leitor(matriz, linha, coluna)
  
  matriz_transposta = calculador_transposta(matriz)
  print('---------------')
  imprimir(matriz_transposta)
  
  vetor_soma = calculador_soma_coluna(matriz)
  print('---------------')
  print(vetor_soma)

  triangular = matriz_triangular(matriz)
  print('---------------')
  print(triangular)

main()