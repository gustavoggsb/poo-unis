while (True):
  a = int(input('Digite o valor de "a": '))
  b = int(input('Digite o valor de "b": '))
  c = int(input('Digite o valor de "c": '))

  if(a < 0) or (b < 0) or (c < 0):
      print('Os valores devem ser maiores que zero.')
      continue

  number = a
  if(b < number):
      number = b
  if(c < number):
      number = c
  
  print('O menor número é: ', number)
  break