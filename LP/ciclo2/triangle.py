while (True):
  a = float(input('Digite o valor de "a": '))
  b = float(input('Digite o valor de "b": '))
  c = float(input('Digite o valor de "c": '))

  if(a < 0):
      print('O valor de "a" é inválido!')
      continue
  if(b < 0):
      print('O valor de "b" é inválido!')
      continue
  if(c < 0):
      print('O valor de "c" é inválido!')
      continue

  if (a + b < c) or (a + c < b) or (b + c < a):
    print ('Os valores a={}, b={} e c={}, não formam um triângulo!'.format(a, b, c))
    break
  elif (a == b) and (a == c): 
    area = (a * b) / 2
    print('Triangulo Equilatero. Area = {}'.format(area))
    break
  elif(a == b) or (a == c) or (b == c): 
    area = (a * b) / 2
    print('Triangulo Isósceles. Area = {}'.format(area))
    break
  else:
    area = (a * b) / 2
    print('Triangulo Escaleno. Area =  {}'.format(area))
    break