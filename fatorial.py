#Faça um programa iterativo (sem recursividade) que calcule o fatorial de um número
#inteiro fornecido pelo teclado. Lembrete: 0! = 1. O fatorial de um número N é calculado
#pela expressão:
#N! = N*(N-1)*(N-2)*(N-3)*...1
n = int(input('Digite um numero para calcular seu fatoreal: '))
c = n 
f = 1
print('Caulculando {}! = '.format(n),end=' ')
while(c > 0):
  print('{}'.format(c), end=' ')
  print(' X ' if(c>1)else( ' = '), end=' ') # Parte visual do programa, end não salta linha 
  f *= c
  c -= 1
print('{}'.format(f)) #  mostrando fatoreal 