def firstRepeatedElement(arr, n):
  #indice do primeiro elemento do array
  Min = -1

  #criando um hashset vazio
  myset = dict()

  #percorrendo o array da direita pra esquerda

  for i in range(n-1, -1, -1):

    if arr[i] in myset.keys():
      Min = i
    
    else:
      myset[arr[i]] = 1

  if (Min != -1):
    print(arr[Min])
  else:
    print(None)


arr = [5, 2, 3, 2, 5]
n = len(arr)
firstRepeatedElement(arr, n)