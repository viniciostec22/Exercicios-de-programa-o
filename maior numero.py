#Faça um programa que leia dois números do teclado e exiba o maior deles.
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
if n1 > n2:
  print('O maior numero é o {}'.format(n1))
else:
  print('o maior numero é o {}'.format(n2))