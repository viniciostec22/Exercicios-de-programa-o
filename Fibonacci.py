 # Faça um programa iterativo (sem recursividade) que receba um valor inteiro N e mostre
 # o n-ésimo termo da série de Fibonacci. Ex.: para N=4 mostre o quarto termo da série.
 # Um número da série de Fibonacci é gerado a partir da soma dos dois valores
 # imediatamente anteriores. Por convenção, o primeiro número da série é 0 e o segundo
 # é 1. A partir desses valores é possível calcular o n-ésimo elemento da série utilizando a
 # seguinte expressão:
 # fn = fn-1+fn-#2
n = int(input('Digite um numero para ver sua sequencia fibonacci: '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3 # contador inicia com com 3 pois ja tenho os dois primeiros termos
while(cont <= n):
  t3 = t1 + t2
  print(' -> {}'.format(t3), end='')
  t1 = t2
  t2 = t3
  cont += 1
  
print(' -> Fim')